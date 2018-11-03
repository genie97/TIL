## CPU 성능

**Exection time (실행시간)**

하나의 작업을 수행하는데 걸리는 시간

**Throughput (처리량)**

단위 시간 당 얼마만큼의 일을 처리할 수 있는지



> Q1. 프로세서를 더 빠른 버전으로 대체하면?
>
> A1.실행시간이 빨라지고 처리량이 증가한다
>
> Q2. 프로세서 코어를 추가하면?
>
> A2실행시간에는 영향을 주지 않고, 처리량이 증가한다

------

**상대적 성능**

```
성능 = 1/실행시간
성능X/성능Y = 실행시간Y/실행시간X = N
```

------

**CPU 클럭 사이클**

일정한 속도로 관리되는 디지털 하드웨어의 operation 시계

```
Clock Period: 시계 주기
Clock Frequency (Rate) = 1/(Clock Period)
단위: cycles per second(Hz)
```

------

**성능 측정 방식**

1. 프로그램 실행 시간: cpu processing, I/O처리 등의 모든 실행 시간을 말한다 
2. CPU 시간: CPU가 주어진 일을 처리하는데 걸리는 시간

------

**CPU Time**

```
CPU Time = CPU Clcok Cycle X Clock Cycle Time
         = CPU Clock Cycle / Clock Rate
         = Instruction Count X CPI X Clock Cycle Time
         = Instruction Count X CPI / Clock Rate
```

------

**프로세서를 위한 두가지 기술**

1. Multi-core processor
2. <u>**Pipelining**</u>



**성능 이슈**

모든 instruction은 하나의 cpu cycle에서 실행된다.

- 가장 긴 딜레이는 clock period를 결정한다
- Critical path 명령어 load: I-type은 **5step**, 다른 instruction들은 **4-step**

------

**파이프라인 기법**

: 병렬성을 이용하여 성능을 개선하기

> Five Step
>
> 1. **IF**: 명령어를 메모리로부터 **fetch**한다
> 2. **ID**: 명령어를 **decode**하고, 레지스터를 읽는다
> 3. **EX**: 작업을 **실행(execution)**하거나 주소를 **계산(calculate)**한다
> 4. **MEM**: 메모리 operand에 **접근(access)**한다
> 5. **WB**: 결과 값을 레지스터에 **write**한다

**파이프라인 속도 향상**

만약 모든 단계가 균형적이라면,  모두 같은 시간이 걸릴 것이다.

```
Time between instructions = Time between instrictions/number of stages(5)
```

하지만 파이프라인의 5단계에서는 단지 4배의 향상이 있었다.

이유

> 1. 불균형
>
>    레지스터를 읽고 쓰는 시간-100ps
>
>    메모리 접근과 산술논리연산-200ps
>
> 2. Overhead
>
>    파이프라인 hazard: 예상보다 시간이 더 걸리는 현상이 있을 수 있다

파이프라인의 속도향상은 **처리량의 증가 때문**이다