## Spring Boot OAuth2 구현

1. Google 로그인

- 프로젝트 구조

![](./images/WEB_IMG/project_structure.PNG)

- 의존성 (build.gradle)

```java
...
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    implementation 'org.springframework.boot:spring-boot-starter-oauth2-client'
    implementation 'org.springframework.boot:spring-boot-starter-security'
    implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-web-services'
    compileOnly 'org.projectlombok:lombok'
    developmentOnly 'org.springframework.boot:spring-boot-devtools'
    runtimeOnly 'com.h2database:h2'
    annotationProcessor 'org.projectlombok:lombok'
    testImplementation('org.springframework.boot:spring-boot-starter-test') {
        exclude group: 'org.junit.vintage', module: 'junit-vintage-engine'
    }
    testImplementation 'org.springframework.security:spring-security-test'
}
...
```

- application.yml

```
spring:
  h2:
    console:
      enabled: true
      path: /console
  thymeleaf:
    cache: false
  security:
    oauth2:
      client:
        registration:
          google:
            client-id: {구글api아이디}
            client-secret: {구글api시크릿키}
```

- DemoApplication

```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

}

```

- SecurityConfig

```java
package com.example.demo.security;

import lombok.Value;
import org.springframework.boot.autoconfigure.security.oauth2.client.OAuth2ClientProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.oauth2.client.CommonOAuth2Provider;
import org.springframework.security.oauth2.client.registration.ClientRegistration;
import org.springframework.security.oauth2.client.registration.ClientRegistrationRepository;
import org.springframework.security.web.authentication.LoginUrlAuthenticationEntryPoint;

import static com.example.demo.security.SocialType.*;


public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    public void configure(HttpSecurity httpSecurity) throws Exception {
        httpSecurity.authorizeRequests()
                .antMatchers("/", "/oauth2/**", "/login/**", "/css/**",
                        "/images/**", "/js/**", "/console/**", "/favicon.ico/**")
                .permitAll()
                .antMatchers("/google").hasAuthority(GOOGLE.getRoleType())
                .anyRequest().authenticated()
                .and()
                .oauth2Login()
                .userInfoEndpoint()
                .and()
                .defaultSuccessUrl("/loginSuccess")
                .failureUrl("/loginFailure")
                .and()
                .exceptionHandling()
                .authenticationEntryPoint(new LoginUrlAuthenticationEntryPoint("/login"));
    }

    private ClientRegistration getRegistration(OAuth2ClientProperties clientProperties, String client) {
        if ("google".equals(client)) {
            OAuth2ClientProperties.Registration registration = clientProperties.getRegistration().get("google");
            return CommonOAuth2Provider.GOOGLE.getBuilder(client).clientId(registration.getClientId()).clientSecret(registration.getClientSecret()).scope("email", "profile").build();
        }
        return null;
    }

}

```

- SocialType

```java
package com.example.demo.security;

public enum SocialType {
    GOOGLE("google");

    private final String ROLE_PREFIX = "ROLE_";
    private String name;

    SocialType(String name) {
        this.name = name;
    }

    public String getRoleType() {
        return ROLE_PREFIX + name.toUpperCase();
    }

    public String getValue() {
        return name;
    }

    public boolean isEquals(String authority) {
        return this.getRoleType().equals(authority);
    }

}

```

