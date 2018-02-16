# Remote Robot Framework Environment Library
RobotRemoteServer를 Import한 Remote(Server/Agent) 환경에서 작동한다.

## Listener
RF는 Command를 Listener가 기둥처럼 서있어서 모두 듣게 된다. 이를 통해 RIDE도 만들어졌다. 

하나의 Suite이나 전체 Suite이 끝나면 Close 신호를 보내는데, 이를 이용해 모든 테스트 후의 작업을 입맛에 맞게 작성 할 수 있다. 

Fail Case만 재시도 해주는 Pybot Argument가 있지만 다수의 재시도, 특정 Case 재시도등 여러가지 시나리오를 통해 테스트가 끝난 유휴 시간에도 회귀테스트를 할 수 있다.   

- TestRunnerAgent_close_PoC.py
```Python
def close(self):
    with open('c:\\bar.txt', 'w') as f:
        self.content = "After All-test suites when test"
        f.write(self.content)
```

- Heartbeat.py

```Python
def close(self):
	with open("c:\\test_close.txt", "w") as f:
		f.write("close test gogo")
	self.outfile.close()
```

## Remote Library
Python으로 작성한 Remote-RF 환경에서 활용 가능한 라이브러리
- LibAgentDownloader: 특정 파일을 다운로드
- LibHosts: Hosts 파일을 조작
- LibYearsManipulate: 날짜를 조작
