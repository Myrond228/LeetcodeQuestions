class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        rows, cols = len(image), len(image[0])
        source = image[sr][sc]

        def floodFill(image, sr, sc):
            if sr<0 or sr>=rows or sc<0 or sc>= cols:
                return
            if image[sr][sc] != source:
                return

            image[sr][sc] = color

            floodFill(image, sr, sc-1)
            floodFill(image, sr, sc+1)
            floodFill(image, sr-1, sc)
            floodFill(image, sr+1, sc)

        floodFill(image, sr, sc)
        return image
