import musicpy.algorithms as algorithms
import musicpy.structures as structures

# chord_notes, chord_inds = algorithms.chord_analysis(structures.chord(['C4', 'E4', 'G4', 'F4', 'A5', 'C5'], 0.5, [0, 0, 0, 5, 5, 5]), is_chord=True, get_original_order=True, mode='chords')
# result = [algorithms.detect(each) for each in [chord_notes[k[0]:k[1]] for k in chord_inds]]
# print([i if not isinstance(i, list) else i[0] for i in result])
# inds = [[i[0], i[1]] for i in chord_inds]
# print([chord_notes.count_bars(k[0], k[1]) for k in inds])

while True:
    chord_notes, chord_inds = algorithms.chord_analysis(
        structures.chord(input().split(','), input().split(','), input().split(',')), 
        is_chord=True, mode='chords', get_original_order=True
    )
    result = [algorithms.detect(each) for each in [chord_notes[k[0]:k[1]] for k in chord_inds]]
    for i in result:
        print(i if not isinstance(i, list) else i[0], end=',')
    print(flush=False)
    inds = [[i[0], i[1]] for i in chord_inds]
    for k in inds:
        bar_range = chord_notes.count_bars(k[0], k[1])
        print(bar_range[0], end=',')
        print(bar_range[1], end=',')
    print()
