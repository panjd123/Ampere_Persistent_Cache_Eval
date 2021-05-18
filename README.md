# Ampere Persistent Cache Eval

Here is an unoffical Ampere persistent L2 cache evaluation

https://developer.download.nvidia.com/video/gputechconf/gtc/2020/presentations/s21819-optimizing-applications-for-nvidia-ampere-gpu-architecture.pdf

## Compile and Run

```bash
nvcc -std=c++11 main.cu -arch=sm_80 && ./a.out
```


## Results

Warning: All tests do not lock core frequency and memory frequency.

### Baseline

| Freq Size (Byte)	| Persistant   Cache Size (Byte)	| Time (ms) 	|
|:-:	|:-:	|:-:	|
| 10 	| 0 	| 40.101921 	|
| 20 	| 0 	| 54.422207 	|
| 30 	| 0 	| 66.159889 	|
| 40 	| 0 	| 76.17881 	|
| 50 	| 0 	| 81.65992 	|
| 60 	| 0 	| 85.687294 	|

| Freq Size (Byte)	| Persistant   Cache Size (Byte)	| Time (ms) 	| Acceleration   Ratio 	|
|:-:	|:-:	|:-:	|:-:	|
| 10 	| 10 	| 32.310387 	| 1.241146415 	|
| 20 	| 20 	| 41.663773 	| 1.306223683 	|
| 30 	| 30 	| 49.951725 	| 1.324476562 	|
| 40 	| 30 	| 60.225136 	| 1.264900589 	|
| 50 	| 30 	| 68.075066 	| 1.199556971 	|
| 60 	| 30 	| 73.440689 	| 1.16675504 	|


