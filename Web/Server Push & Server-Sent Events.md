## 서버 푸시 (Server Push)와 SSE (Server-Sent Events) 

1. 서버 푸시(Server Push) 란?

   > 서버에서 클라이언트로 데이터를 전송해주는 통신 방식을 말한다
   >
   > 데이터 전송 방향이 **서버**에서 **클라이언트**로 이루어진다

   > 서버 푸시와 반대되는 개념이 **클라이언트 (Client Polling)** 이다
   >
   > 폴링의 데이터 전송 방향은 **클라이언트**에서 **서버**이다

2. SSE (Server-Sent Events) 란?

   > 기존 방식의 문제점을 해결하여, 서버가 필요할 때마다 클라이언트에게 
   >
   > 데이터를 줄 수 있게 해주는 서버 푸시 기술을 말한다

   > 기존 방식의 문제점을 해결하여, 서버가 필요할 때마다 클라이언트에게 
   >
   > 데이터를 줄 수 있게 해주는 서버 푸시 기술을 
   >
   > HTML5가 등장하기 전까지는 서버 푸시를 위한 표준화 기술이 없었다
   >
   > - 기존에 실시간 정보를 받아오기 위해 사용한 방식 
   >   - 외부 플러그인 이용
   >     문제점 : 플러그인을 설치해야한다는 불편함
   >   - 서버 푸시를 흉내 낸 Ajax 폴링 기법 
   >     문제점 : 쓸모없는 요청 발생으로 인한 대역폭의 낭비가 발생 
   >     (HTTP 오버헤드 증가)

3. SSE의 장점

   > - 전통적인 HTTP를 통해 통신하여 다른 프로토콜이 필요 없다
   > - 재접속 처리 등과 같은 저수준 처리가 자동으로 가능하다
   > - IE를 제외한 브라우저 대부분을 지원한다 (Firefox 6.0, Chrome 6.0, Safari 5.0 등)
   > - HTML과 JavaScript만으로 구현 가능하다

4. 예시

   **클라이언트**

   > - 서버 호출은 EventSource() 객체 생성으로 시작되고, 호출하고자 하는 서버측 URL을 전달한다
   >
   > - 서버와의 연결이 성공하면 **onopen 이벤트**가 발생한다
   >
   > - 서버에서 메시지가 도착하면 **onmessage 이벤트**가 발생한다
   >
   > - 서버와의 연결이 종료되거나 오류가 발생하면 **onerror 이벤트**가 발생한다
   >
   >
   > ```html
   > function() {
   > 					//EventSource 생성 및 서버 호출
   > 					eventSource = new EventSource(
   > 							"http://localhost:8080/SSE/examServer.jsp");
   > 					
   > 					//서버와의 연결이 open되면 호출됨
   > 					eventSource.onopen = function(event) {
   > 						doument.getElementById("state").innerHTML = "STARTED";
   > 					};
   > 					//서버에서 메시지가 도착하면 호출됨
   > 					eventSource.onmessage = function(event) {
   > 						document.getElementById("time").innerHTML = event.data;
   > 					};
   > 					//서버와의 연결이 끊기거나 오류가 발생하면 호출
   > 					eventSource.onerror = function(event) {
   > 						documen.getElementById("state").innerHTML = "ERROR";
   > 					};
   > 				});
   > ```

   

   **서버**

   > 클라이언트에 데이터를 push하기 위해서는 응답요청의 content-type을 **text/event-stream**으로 설정하고, 컨텐츠를 **utf-8**로 인코딩한 후 전송한다	
   >
   > ```jsp
   > <% response.setContentType("text/event-stream;charset=UTF-8"); %>
   > ```
   >
   > 서버에서 전송되는 컨텐츠 파싱 규칙
   >
   > - 라인 시작문자가 콜론 (:) 일 경우 무시한다
   > - 라인에 콜론 (:) 이 포함된 경우 : 라인부터 콜론 (:) 까지를 **필드명**으로 파싱하고, 콜론 (:) 이후부터 라인의 끝까지를 **필드값** 으로 파싱한다
   > - 라인에 콜론 (:) 이 없는 경우 : **라인 전체**를 **필드명**으로 파싱하고 **필드값**은 **빈 값**으로 설정한다
   >
   > 필드명 규칙 
   >
   > - 필드명이 **event**인 경우 : evnetbuffer에 필드값을 <u>저장한다</u> (set)
   > - 필드명이 **data**인 경우 : databuffer에 필드값을 <u>덧붙인다</u> (append)
   > - 필드명이 **id**인 경우 : lasteventIDbuffer에 필드값을 <u>저장한다</u> (set)
   > - 필드명이 **retry**, 필드값이 **숫자**인 경우 :  reconnectiontime (ms)의 값으로 필드값을 <u>설정한다</u> (set)
   > - **필드명이 위의 네가지가 아닌 경우는 무시한다**
   >
   > 공백 라인이 있는 경우 event, data, id 값들이 클라이언트의 onmessage 이벤트로 dispatch 된다
   >
   > - onmessage 이벤트로 dispatch 되면 관련 버퍼들은 모두 초기화 된다
   > 	 evnet 필드가 존재하는 경우 해당 event 필드값과 동일한 이름의 이벤트를 실행한다		 	

