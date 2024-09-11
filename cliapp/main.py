from fastapi import FastAPI

app = FastAPI()

@app.get("/container/ls")
# docker container ls 명령어의 실행 결과를 반환
def container_ls():
    import subprocess
    output = subprocess.check_output("docker container ls", shell = True)
    return output.decode("utf-8")

@app.get("/container/run")
def container_run():
    import subprocess
    output = subprocess.check_output(f"docker container run --rm -P -d nginx", shell=True)
    output = output.decode("utf-8").strip()
    output = subprocess.check_output(f"docker container ls  -f id={output}", shell=True)
    return output.decode("utf-8")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host = "127.0.0.1", port = 80, log_level = "debug", reload = True)