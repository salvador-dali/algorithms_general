# https://www.interviewbit.com/problems/largest-rectangle-in-histogram/
# http://prismoskills.appspot.com/lessons/Arrays/Largest_rectangle_under_histogram.jsp
# http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
# https://www.quora.com/What-is-the-algorithmic-approach-to-find-the-maximum-rectangular-area-in-a-histogram
# http://tech-queries.blogspot.com/2011/03/maximum-area-rectangle-in-histogram.html
# http://stackoverflow.com/q/4311694/1090562
def largestRect(histogram):
    stack, max_area, pos = [], 0, 0
    for pos, height in enumerate(histogram):
        start = pos
        while True:
            if not stack or height > stack[-1][1]:
                stack.append((start, height))
                break

            max_area = max(max_area, stack[-1][1]*(pos-stack[-1][0]))
            start, _ = stack.pop()

    pos += 1
    for start, height in stack:
        print height
        max_area = max(max_area, height*(pos-start))

    return max_area
