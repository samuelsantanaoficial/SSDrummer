import mido
import os

# Obtém o diretório do script
dir_path = os.path.dirname(os.path.abspath(__file__))

for file_name in os.listdir(dir_path):
    if file_name.endswith('.mid'):
        midi_path = os.path.join(dir_path, file_name)
        midi = mido.MidiFile(midi_path)

        for track in midi.tracks:
            for msg in track:
                if msg.type in ('note_on', 'note_off', 'control_change'):
                    msg.channel = 9  # Canal 10 (baseado em zero)

        # Salva o arquivo convertido com prefixo 'converted_'
        converted_path = os.path.join(dir_path, f"{file_name}")
        midi.save(converted_path)
        print(f"Convertido: {file_name} -> {converted_path}")

