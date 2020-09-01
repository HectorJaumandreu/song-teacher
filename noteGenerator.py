import numpy as np, music21, simpleaudio as sa, soundfile as sf

def generateNotes():
    """ Provides 7 .wav files with the note from C to B
    """
    fs = 44100 # hertz
    seconds = 3  # Note duration of 3 seconds
    noteNames = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]
    for noteName in noteNames:
        myNote = music21.note.Note(noteName)
        noteFrequency = myNote.pitch.frequency
        # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
        t = np.linspace(0, seconds, seconds * fs, False)

        # Generate a 440 Hz sine wave
        sound = np.sin(noteFrequency * t * 2 * np.pi)

        # Ensure that highest value is in 16-bit range
        audio = sound * (2**15 - 1) / np.max(np.abs(sound))
        # Convert to 16-bit data
        audio = audio.astype(np.int16)

        # Start playback
        play_obj = sa.play_buffer(audio, 1, 2, fs)

        # Wait for playback to finish before exiting
        play_obj.wait_done()

        #Write sound to file
        sf.write('assets/patterns/'+noteName+'.wav', audio, fs)






"""
        obj = wave.open('assets/patterns/'+noteName+'.wav','w')
        obj.setnchannels(1) # mono
        obj.setsampwidth(2)
        obj.setframerate(sampleRate)
        for i in range(duration*sampleRate):
            data = struct.pack('<h', int(noteFrequency))
            obj.writeframesraw( data )
        obj.close()

"""