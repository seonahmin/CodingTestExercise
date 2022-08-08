from collections import defaultdict
def solution(participant, completion):
    p = defaultdict(int)
    for part in participant:
        p[part] += 1
    for c in completion:
        p[c] -= 1
    for p_k, p_v in p.items():
        if p[p_k] > 0:
            return p_k

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
