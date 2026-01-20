FROM python:3.11-slim
WORKDIR /app
COPY cpu_benchmark.py run.sh /app/
RUN chmod +x /app/run.sh
CMD ["/app/run.sh"]
