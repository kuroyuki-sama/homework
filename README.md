프로그래밍II 6팀 과제 제출용

해당 파일로이동
cd homework
^^ 얘들은 cd 뒤에 자신이 이동할 디렉토리명을 적으면 됨.

① 원격 저장소의 브랜치 정보 가져오기
git fetch origin


GitHub에 새롭게 만들어진 브랜치 정보를 로컬로 가져오는 명령어야.

② 자신의 브랜치로 이동하기

팀원 A라면 다음과 같이 입력해.
git switch --track origin/feature-A


팀원 B라면 다음과 같이 입력하면 돼.
git switch --track origin/feature-B


이 명령어를 실행하면 로컬에 해당 브랜치가 연결되고 자동으로 이동하게 돼.

③ 현재 브랜치 확인하기
git branch


예를 들어 다음과 같이 나온다면 성공이야.
  main
* feature-A
  feature-B
  feature-C


여기서 * 표시가 현재 자신이 작업하고 있는 브랜치야.
