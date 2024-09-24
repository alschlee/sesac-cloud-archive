from fastapi import FastAPI

app = FastAPI()

# 실행 상태의 도커 컨테이너 조회
@app.get("/container/ls")
# docker container ls 명령어의 실행 결과를 반환
def container_ls():
    import subprocess
    output = subprocess.check_output("docker container ls", shell=True)
    return output.decode("utf-8")

# 실행 상태의 도커 컨테이너 목록을 JSON 형식으로 조회
@app.get("/container/ps")
def container_ls():
    import subprocess
    output = subprocess.check_output("docker container ls --format json", shell=True)
    return output.decode("utf-8")

# nginx 컨테이너 생성 후 컨테이너 정보 반환
@app.get("/container/run")
def container_run():
    import subprocess
    output = subprocess.check_output(f"docker container run --rm -P -d nginx", shell=True)
    output = output.decode("utf-8").strip()
    output = subprocess.check_output(f"docker container ls  -f id={output}", shell=True)
    return output.decode("utf-8")

# 80 포트로 실행
# host="0.0.0.0" ~> 모든 IP 주소로 부터의 요청 처리
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="debug", reload=True)