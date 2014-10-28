import math, wave, array

# -------------------------------------- @
start = 50
end = 10000
it = 50
duration = 3 # seconds
sampleRate = 44100 # of samples per second (standard)
numChan = 1 # of channels (1: mono, 2: stereo)
dataSize = 2 # 2 bytes because of using signed short integers => bit depth = 16
# -------------------------------------- #

def sound_gen(sampleRate, numChan, dataSize, freq, duration, f):
    print "generating freq = %d" %(freq)
    volume = 100 # 100 %
    data = array.array('h') # signed short integer (-32768 to 32767) data
    numSamplesPerCyc = int(sampleRate / freq)
    numSamples = sampleRate * duration
    for i in range(numSamples):
        sample = 32767 * float(volume) / 100
        sample *= math.sin(math.pi * 2 * (i % numSamplesPerCyc) / numSamplesPerCyc)
        data.append(int(sample))
    f.writeframes(data.tostring())

buf=array.array('h')

f = wave.open('mix_sound.wav', 'w')
f.setparams((numChan, dataSize, sampleRate, (sampleRate * duration) * ((end-start)/it), "NONE", "Uncompressed"))
for i in range(start, end, it):
    sound_gen(sampleRate, numChan, dataSize, i, duration, f)

f.close()

