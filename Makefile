main: main.cu
	nvcc -o main main.cu -std=c++11 -O3 -arch=sm_80 -lineinfo

ncu:
	ncu --cache-control all --clock-control base --target-processes all --rule SOLBottleneck --set full \
    --import-source on --call-stack \
    -o report-persist.ncu-rep -f \
    ./main 40 40 1
