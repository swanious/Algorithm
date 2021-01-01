def diffWaysToCompute(input):
    # 정복
    def compute(left, right, operator):
        result = []
        for l in left:
            for r in right:
                result.append(eval(str(l) + operator + str(r)))

        return result

    if input.isdigit():
        return [int(input)]

    # 분할, 조합
    results = []
    for index, value in enumerate(input):
        if value in '*+-':
            left = diffWaysToCompute(input[:index])
            right = diffWaysToCompute(input[index + 1:])

            results.extend(compute(left, right, value))
    return sorted(results)

input = input()
a = diffWaysToCompute(input)
print(a)