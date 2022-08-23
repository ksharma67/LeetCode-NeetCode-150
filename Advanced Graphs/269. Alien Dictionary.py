class Solution:
    def alienOrder(self, words: List[str]) -> str:
        words_count = len(words)
        if words_count == 0:
            return ""
        # initialize result list
        ordered_letters = []
        # initialize in degrees and graph as adjacency list
        in_degrees = {}
        graph = {}
        
        # fill default values
        for word in words:
            for letter in word:
                in_degrees[letter] = 0
                graph[letter] = []
        
        # build out graph and in_degrees
        for i in range(words_count - 1):
            # compare the words next to each other since they are sorted lexographically
            word1, word2 = words[i], words[i + 1]
            smaller_word = min(len(word1), len(word2))
            for j in range(smaller_word):
                # basically the letters are like vertices at this point
                parent_letter, child_letter = word1[j], word2[j]
                # if they differ, the parent letter must come before the child letter
                # so add child to parent's list and increment in_degrees for child
                if parent_letter != child_letter:
                    graph[parent_letter].append(child_letter)
                    in_degrees[child_letter] += 1
                    
                    break
                # at end of smaller word and we didnt break out yet
                elif j == smaller_word - 1:
                    if len(word2) < len(word1):
                        return ""
        
        # source = a vertex with only outgoing edges
        sources = collections.deque()
        # add to our queue all sources
        for letter in in_degrees:
            if in_degrees[letter] == 0:
                sources.append(letter)
        
        while sources:
            source = sources.popleft()
            ordered_letters.append(source)
            
            # remove edges going to children
            for child in graph[source]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)
                    
        # if number of letters in sorted list is not equal to number of total distinct letters we have a cycle so its not possible to order
        return "" if len(in_degrees) != len(ordered_letters) else "".join(ordered_letters)
