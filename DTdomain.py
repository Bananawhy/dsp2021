import wave
import numpy as np
import pylab as plt
from scipy.fftpack import fft,ifft
import UIInterface
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from importlib import reload
reload(sys)
# sys.setdefaultencoding('utf-8')
import wave
import numpy as np
import pylab as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog
import pyaudio
import os
#import tensorflow as tf
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from PyQt5 import QtCore, QtGui, QtWidgets
def Lnoise():
    wave_open = wave.open(r"E:/pythonProject1/Project file/Lnoise.wav", "rb")
    #打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV 文件的格式和数据。
#读取格式信息
#一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采
#样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
    params = wave_open.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
#读取波形数据
#读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
    str_data  = wave_open.readframes(nframes)
    wave_open.close()
#将波形数据转换成数组
#需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
    wave_data = np.frombuffer(str_data,dtype=np.int16)
    wave_data = wave_data*1.0/(max(abs(wave_data)))#wave幅值归一化
#通过取样点数和取样频率计算出每个取样的时间。
    time = np.arange(0, nframes)/framerate
# 从波形数据中取样nframes个点进行运算
    xs = wave_data [:nframes]
# xf=np.fft.rfft(xs)
# #于是可以通过下面的np.linspace计算出返回值中每个下标对应的真正的频率：
# freqs=np.linspace(0,framerate/2, nframes/2+1)
    xf= np.fft.fft(xs)
    freqs = np.fft.fftfreq(nframes,1.0/framerate)
    print(params)

    plt.subplot(211)
    plt.plot(time[:nframes], xs)
    plt.xlabel("time(s)")
    plt.title('Original wave')
    plt.subplot(212)
    plt.plot(freqs,np.abs(xf),'r') #显示原始信号的FFT模值
    plt.title('FFT of Mixed wave(two sides frequency range)')
    plt.show()
def Mnoise():
    wave_open = wave.open(r"E:/pythonProject1/Project file/Mnoise.wav", "rb")
    #打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV 文件的格式和数据。
#读取格式信息
#一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采
#样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
    params = wave_open.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
#读取波形数据
#读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
    str_data  = wave_open.readframes(nframes)
    wave_open.close()
#将波形数据转换成数组
#需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
    wave_data = np.frombuffer(str_data,dtype=np.int16)
    wave_data = wave_data*1.0/(max(abs(wave_data)))#wave幅值归一化
#通过取样点数和取样频率计算出每个取样的时间。
    time = np.arange(0, nframes)/framerate
# 从波形数据中取样nframes个点进行运算
    xs = wave_data [:nframes]
# xf=np.fft.rfft(xs)
# #于是可以通过下面的np.linspace计算出返回值中每个下标对应的真正的频率：
# freqs=np.linspace(0,framerate/2, nframes/2+1)
    xf= np.fft.fft(xs)
    freqs = np.fft.fftfreq(nframes,1.0/framerate)
    print(params)

    plt.subplot(211)
    plt.plot(time[:nframes], xs)
    plt.xlabel("time(s)")
    plt.title('Original wave')
    plt.subplot(212)
    plt.plot(freqs,np.abs(xf),'r') #显示原始信号的FFT模值
    plt.title('FFT of Mixed wave(two sides frequency range)')
    plt.show()
def Snoise():
    wave_open = wave.open(r"E:/pythonProject1/Project file/Snoise.wav", "rb")
    #打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV 文件的格式和数据。
#读取格式信息
#一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采
#样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
    params = wave_open.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
#读取波形数据
#读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
    str_data  = wave_open.readframes(nframes)
    wave_open.close()
#将波形数据转换成数组
#需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
    wave_data = np.frombuffer(str_data,dtype=np.int16)
    wave_data = wave_data*1.0/(max(abs(wave_data)))#wave幅值归一化
#通过取样点数和取样频率计算出每个取样的时间。
    time = np.arange(0, nframes)/framerate
# 从波形数据中取样nframes个点进行运算
    xs = wave_data [:nframes]
# xf=np.fft.rfft(xs)
# #于是可以通过下面的np.linspace计算出返回值中每个下标对应的真正的频率：
# freqs=np.linspace(0,framerate/2, nframes/2+1)
    xf= np.fft.fft(xs)
    freqs = np.fft.fftfreq(nframes,1.0/framerate)
    print(params)

    plt.subplot(211)
    plt.plot(time[:nframes], xs)
    plt.xlabel("time(s)")
    plt.title('Original wave')
    plt.subplot(212)
    plt.plot(freqs,np.abs(xf),'r') #显示原始信号的FFT模值
    plt.title('FFT of Mixed wave(two sides frequency range)')
    plt.show()
def Hnoise():
    wave_open = wave.open(r"E:/pythonProject1/Project file/Hnoise.wav", "rb")
    #打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV 文件的格式和数据。
#读取格式信息
#一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采
#样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
    params = wave_open.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
#读取波形数据
#读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
    str_data  = wave_open.readframes(nframes)
    wave_open.close()
#将波形数据转换成数组
#需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
    wave_data = np.frombuffer(str_data,dtype=np.int16)
    wave_data = wave_data*1.0/(max(abs(wave_data)))#wave幅值归一化
#通过取样点数和取样频率计算出每个取样的时间。
    time = np.arange(0, nframes)/framerate
# 从波形数据中取样nframes个点进行运算
    xs = wave_data [:nframes]
# xf=np.fft.rfft(xs)
# #于是可以通过下面的np.linspace计算出返回值中每个下标对应的真正的频率：
# freqs=np.linspace(0,framerate/2, nframes/2+1)
    xf= np.fft.fft(xs)
    freqs = np.fft.fftfreq(nframes,1.0/framerate)
    print(params)

    plt.subplot(211)
    plt.plot(time[:nframes], xs)
    plt.xlabel("time(s)")
    plt.title('Original wave')
    plt.subplot(212)
    plt.plot(freqs,np.abs(xf),'r') #显示原始信号的FFT模值
    plt.title('FFT of Mixed wave(two sides frequency range)')
    plt.show()
def nuonuo():
    wave_open = wave.open(r"E:/pythonProject1/Project file/nuonuo.wav", "rb")
    #打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV 文件的格式和数据。
#读取格式信息
#一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采
#样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
    params = wave_open.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
#读取波形数据
#读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
    str_data  = wave_open.readframes(nframes)
    wave_open.close()
#将波形数据转换成数组
#需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
    wave_data = np.frombuffer(str_data,dtype=np.int16)
    wave_data = wave_data*1.0/(max(abs(wave_data)))#wave幅值归一化
#通过取样点数和取样频率计算出每个取样的时间。
    time = np.arange(0, nframes)/framerate
# 从波形数据中取样nframes个点进行运算
    xs = wave_data [:nframes]
# xf=np.fft.rfft(xs)
# #于是可以通过下面的np.linspace计算出返回值中每个下标对应的真正的频率：
# freqs=np.linspace(0,framerate/2, nframes/2+1)
    xf= np.fft.fft(xs)
    freqs = np.fft.fftfreq(nframes,1.0/framerate)
    print(params)

    plt.subplot(211)
    plt.plot(time[:nframes], xs)
    plt.xlabel("time(s)")
    plt.title('Original wave')
    plt.subplot(212)
    plt.plot(freqs,np.abs(xf),'r') #显示原始信号的FFT模值
    plt.title('FFT of Mixed wave(two sides frequency range)')
    plt.show()
def me():
    wave_open = wave.open(r"E:/pythonProject1/Project file/me.wav", "rb")
    #打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV 文件的格式和数据。
#读取格式信息
#一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采
#样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
    params = wave_open.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
#读取波形数据
#读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
    str_data  = wave_open.readframes(nframes)
    wave_open.close()
#将波形数据转换成数组
#需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
    wave_data = np.frombuffer(str_data,dtype=np.int16)
    wave_data = wave_data*1.0/(max(abs(wave_data)))#wave幅值归一化
#通过取样点数和取样频率计算出每个取样的时间。
    time = np.arange(0, nframes)/framerate
# 从波形数据中取样nframes个点进行运算
    xs = wave_data [:nframes]
# xf=np.fft.rfft(xs)
# #于是可以通过下面的np.linspace计算出返回值中每个下标对应的真正的频率：
# freqs=np.linspace(0,framerate/2, nframes/2+1)
    xf= np.fft.fft(xs)
    freqs = np.fft.fftfreq(nframes,1.0/framerate)
    print(params)

    plt.subplot(211)
    plt.plot(time[:nframes], xs)
    plt.xlabel("time(s)")
    plt.title('Original wave')
    plt.subplot(212)
    plt.plot(freqs,np.abs(xf),'r') #显示原始信号的FFT模值
    plt.title('FFT of Mixed wave(two sides frequency range)')
    plt.show()