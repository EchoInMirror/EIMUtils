import musicpy.algorithms as algorithms
import musicpy.structures as structures

if __name__ == '__main__':
    while True:
        action = input()
        if action == 'chords_detect':
            chord_notes, chord_inds = algorithms.chord_analysis(
                structures.chord(input(), list(map(float, input().split(','))), list(map(float, input().split(',')))),
                is_chord=True, mode='chords', get_original_order=True
            )
            result = [algorithms.detect(each) for each in [chord_notes[k[0]:k[1]] for k in chord_inds]]
            for i in result:
                print(i if not isinstance(i, list) else i[0], end=',')
            print()
            inds = [[i[0], i[1]] for i in chord_inds]
            for k in inds:
                bar_range = chord_notes.count_bars(k[0], k[1])
                print(bar_range[0], end=',')
                print(bar_range[1], end=',')
            print(flush=True)
