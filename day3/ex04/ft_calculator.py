class calculator:
    """My calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Method to do the dot product of two vectors"""
        result = sum(x * y for x, y in zip(V1, V2))
        # for x, v in enumerate(V1):
        #     result = result + (v * V2[x])
        print(result)
        return result

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Method to add two vectors together"""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(result)
        return result

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Method to substract two vectors together"""
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(result)
        return result
