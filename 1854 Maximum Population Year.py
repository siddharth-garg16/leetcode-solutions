class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_record = [0]*101

        #---brute force solution O(n^2) time complexity-----
        # for i in range(len(logs)):
        #     for j in range(logs[i][0], logs[i][1]):
        #         population_record[j-1950] += 1
                
        # max_population = max(population_record)
        
        # for i in range(len(population_record)):
        #     if population_record[i] == max_population:
        #         return (i+1950)

        #---running some of array concept O(n) T.C.------
        for i in range(len(logs)):
            population_record[logs[i][0]-1950] += 1
            population_record[logs[i][1]-1950] -= 1
        
        for i in range(1, len(population_record)):
            population_record[i] += population_record[i-1]
            
        max_pop = 0
        max_pop_year = 1950
        for i in range(len(population_record)):
            if population_record[i] > max_pop:
                max_pop = population_record[i]
                max_pop_year = i+1950
                
        return max_pop_year

