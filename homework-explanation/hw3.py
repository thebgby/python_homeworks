txt = 'abcabcdabcdeabcdefabcdefg'
# abc_abcd_abcdeab_cdef_abcdefg
# abc_abcd_abcdeab_cdef_abcdefg
done = "aeiou"
# done = {'a', 'e', 'i', 'o', 'u'}
counter = 0

# ans = ""
ans = []

for i in range(len(txt)):
    counter += 1
    # ans += txt[i]
    ans.append(txt[i])
    if i!=len(txt)-1 and counter >= 3 and txt[i] not in done:
        done += txt[i]
        # ans += "_" # ans = ans + '_'
        ans.append('_')
        counter = 0

print(''.join(ans))