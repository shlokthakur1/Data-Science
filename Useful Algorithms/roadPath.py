def convert(list):
    """
    Functionality of the function: converts a list into the string
    Time complexity: O(N) where N is the length of the list
    Space complexity: O(N) where N is the length of the list
    Error handle: None
    Return: None
    Parameter: list- the list that wants to be converted into a string
    Precondition: list must be a list data structure
            """
    string = ""
    for x in list:
        string += x
    return string

class MinHeap:
    def __init__(self, aList):
        self.heap = [0]
        for i in aList:
            self.heap.append(i)
            self.rise(len(self.heap) - 1)

    def pop(self):
        """
        Functionality of the function: Pops out the minimum value of the heap
        Time complexity: O(1)
        Space complexity: O(1)
        Error handle: None
        Return: the root of the MinHeap which is the minimum value
        Parameter: None
        Precondition: There must be nodes in the heap
        """
        if len(self.heap)>2:
            self.swap(1, len(self.heap)-1)
            max = self.heap.pop()
            #print(max.distance)
            self.sink(1)
        else:
            max = self.heap.pop()
        return max

    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def rise(self, index):
        """
        Functionality of the function: Checks to see if the parents are greater than the current index,
        depending on the outcome it swaps or not

        Time complexity: log(N) where N is the number of parents in the heap
        Space complexity: N where N is the number of nodes in the heap
        Error handle: None
        Return: None
        Parameter:index: index of the position we want to rise up the heap
        Precondition: index must be an integer
        """
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index].distance < self.heap[parent].distance:
            self.swap(index,parent)
            self.rise(parent)

    def sink(self, index):
        """
        Functionality of the function: Checks to see if the childs are smaller than the current index,
        depending on the outcome it swaps or not
        Time complexity:log(N) where N is the number of children in the heap
        Space complexity: N where N is the number of nodes in the heap
        Error handle: None
        Return: None
        Parameter:index: index of the position we want to sink down the heap
        Precondition: index must be an integer
        """
        left_child = index * 2
        right_child = index * 2 + 1
        largest_node = index
        n = len(self.heap)

        if left_child < n and self.heap[largest_node].distance > self.heap[left_child].distance:
            largest_node = left_child

        if right_child<n and self.heap[largest_node].distance > self.heap[right_child].distance:
            largest_node = right_child

        if largest_node != index:
            self.swap(index,largest_node)
            self.sink(largest_node)
            
class edge:
    def __init__(self,point2,weight):
        """
        Functionality of the function
        Time complexity:
        Space complexity:
        Error handle:
        Return:
        Parameter:
        Precondition:
        """
        self.u = point2
        self.w = weight
        self.toll = False

class vertex:
    def __init__(self,id):
        """
        Functionality of the function
        Time complexity:
        Space complexity:
        Error handle:
        Return:
        Parameter:
        Precondition:
        """
        self.id = id
        self.edge_list = []
        self.distance = 0
        self.connection = None #or should it be self
        self.camera = False
        self.service = False
        self.discovered = False
        self.finalised = False

    def add_edge(self,point2,weight):
        """
        Functionality of the function
        Time complexity:
        Space complexity:
        Error handle:
        Return:
        Parameter:
        Precondition:
        """
        self.edge_list.append((point2,weight))

class graph:
    def __init__(self):
        self.no_vertices = 0
        self.vertex_list = []
        self.count = 0
        self.service_list = []
        self.buildList = []
        self.filename = ""
        self.old_vertex_list = []

    def resetVertices(self):
        for i in self.vertex_list:
            i.discovered = False
            i.finalised = False

    def new_vertex(self,id):
        """
        Functionality of the function: Add a vertex to the graph
        Time complexity: O(1)
        Space complexity: O(1)
        Error handle: None
        Return: None
        Parameter: id- the id of the vertex in the graph
        Precondition: id must be an integer
        """
        self.vertex_list[id] = vertex(id)
        self.count += 1

    def new_edge(self,point1,point2,weight):
        """
        Functionality of the function: add a new edge to the vertex
        Time complexity: O(1)
        Space complexity: O(1)
        Error handle: None
        Return: None
        Parameter:  point1- vertex where the edge starts from
                    point2- vertex where the edge goes to
                    weight- the weight of the edge
        Precondition: point1 should be a vertex id, point2 should be a vertex id, weight should be an integer
        """
        E = edge(point2,weight)
        self.vertex_list[point1].edge_list.append(E)

    def buildGraph(self,filename):
        """
        Functionality of the function: builds the graph
        Time complexity: O(EV) where E is the total number of edges and V is the total number of vertices
        Space complexity: O(E+V) where E is the total number of edges and V is the total number of vertices
        Error handle: None
        Return: None
        Parameter: filename- the name of the file which contains all the edges
        Precondition: filename must be a string
        """
        self.filename = filename
        with open(filename) as file:
            fileList = file.read().splitlines()
        self.buildList = fileList
        input_edge = []
        for i in fileList:
            j = i.split()
            input_edge.append(j)
        vertixList = []
        for i in range(len(input_edge)):
            if input_edge[i][0] not in vertixList:
                vertixList.append(input_edge[i][0])
            if input_edge[i][1] not in vertixList:
                vertixList.append(input_edge[i][1])
        self.no_vertices = len(vertixList)
        self.vertex_list = [None] * self.no_vertices

        for i in range(len(vertixList)):
            self.new_vertex(int(vertixList[i]))

        for i in input_edge:
            point1 = int(i[0])
            point2 = int(i[1])
            weight = float(i[2])
            self.new_edge(point1, self.vertex_list[point2], weight)

    def quickestPath(self,source,target):
        """
        Functionality of the function: finds the quickest path from source to target by using Djikstra and then traversing
        through the graph
        Time complexity:O(E*log V) where E is the total number of edges and V is the total number of vertices
        Space complexity:O(E + V) where E is the total number of edges and V is the total number of vertices
        Error handle: None
        Return: The actual path and the
        Parameter:  source- the vertex where we want to being our shortest path problem from
                    target- the vertes where we want the shortest path problem to finish
        Precondition:source must be an integer
                    target must be an integer
        """
        self.resetVertices()
        finalised = []
        discovered = []
        discovered.append(self.vertex_list[source])
        self.vertex_list[source].discovered = True
        self.vertex_list[source].distance = 0
        while len(discovered) != 0:
            M = MinHeap(discovered)
            v = M.pop()
            v.discovered = True
            edge_list = v.edge_list
            for i in range(len(edge_list)):
                cur_edge = edge_list[i]
                u = cur_edge.u
                w = cur_edge.w
                if u.discovered == False and u.finalised == False:
                    discovered.append(u)
                    u.distance = v.distance + w
                    u.connection = v
                    u.discovered = True
                elif u.distance > v.distance + w:
                    u.distance = v.distance + w
                    u.connection = v
            finalised.append(v)
            discovered.remove(v)
            v.finalised = True

        if len(finalised)==1:
            return ((None,-1))
        time = 0
        for i in finalised:
            if i.id == target:
                time = i.distance

        reversedPath = []
        current = self.vertex_list[target]
        reversedPath.append(current.id)
        while current.id != source:
            reversedPath.append(current.connection.id)
            current = current.connection
        path = []
        for i in range(len(reversedPath)-1,-1,-1):
            path.append(reversedPath[i])

        string = ""
        for i in range(len(path)):
            string += str(path[i])
            if i < len(path)-1:
                string += " -> "
        return ((string,time))

    def Reverse_quickestPath(self,source,target):
        """
        Functionality of the function: finds the quickest path from target to source by using Djikstra and then traversing
        through the graph
        Time complexity:O(E*log V) where E is the total number of edges and V is the total number of vertices
        Space complexity:O(E + V) where E is the total number of edges and V is the total number of vertices
        Error handle: None
        Return: The actual path and the
        Parameter:  source- the vertes where we want the shortest path problem to finish
                    target- the vertex where we want to being our shortest path problem from
        Precondition:source must be an integer
                    target must be an integer
        """
        self.resetVertices()
        finalised = []
        discovered = []
        discovered.append(self.vertex_list[source])
        self.vertex_list[source].distance = 0
        self.vertex_list[source].discovered = True
        while len(discovered) != 0:
            M = MinHeap(discovered)
            v = M.pop()
            v.discovered = True
            edge_list = v.edge_list
            for i in range(len(edge_list)):
                cur_edge = edge_list[i]
                u = cur_edge.u
                w = cur_edge.w
                if u.discovered == False and u.finalised == False:
                    discovered.append(u)
                    u.distance = v.distance + w
                    u.connection = v
                    u.discovered = True
                elif u.distance > v.distance + w:
                    u.distance = v.distance + w
                    u.connection = v
            finalised.append(v)
            v.finalised = True
            discovered.remove(v)

        time = 0
        for i in finalised:
            if i.id == target:
                time = i.distance

        reversedPath = []
        current = self.vertex_list[target]
        reversedPath.append(current.id)
        while current.id != source:
            # print(current.id)
            reversedPath.append(current.connection.id)
            current = current.connection

        string = ""
        for i in range(len(reversedPath)):
            string += str(reversedPath[i])
            if i < len(reversedPath) - 1:
                string += " -> "
        return ((string, time))

    def augmentGraph(self,camerafilename,tollfilename):
        """
        Functionality of the function: add cameras and tolls to the graph, to the vertex or toll respectively
        Time complexity:O(C+T) where C is the total number of cameras and T is the total number of tolls
        Space complexity:O(C+T) where C is the total number of cameras and T is the total number of tolls
        Error handle: None
        Return: None
        Parameter:  camerafilename which is the name of the file containing all the vertices which have cameras
                    tollfilename which is the name of the file containing all the edges which have tolls
        Precondition: camerafilename and tollfilename should be a string
        """
        with open(camerafilename) as camera_file:
            camera_list = camera_file.read().splitlines()
        for i in camera_list:
            v = self.vertex_list[int(i)]
            v.camera = True
        with open(tollfilename) as toll_file:
            toll_list = toll_file.read().splitlines()
        input_toll = []
        for i in toll_list:
            j = i.split()
            input_toll.append(j)
        for i in input_toll:
            v = self.vertex_list[int(i[0])]
            for k in v.edge_list:
                if k.u.id == int(i[1]):
                    k.toll = True

    def resetGraph(self):
        """
        Functionality of the function resets a graph to have no vertices and therefore no edges
        Time complexity: O(1)
        Space complexity:O(1)
        Error handle: None
        Return: None
        Parameter: None
        Precondition: None
        """
        self.no_vertices = 0
        self.vertex_list = []
        self.count = 0

    def quickestSafePath(self, source, target):
        """
        Functionality of the function: find the quickest safest path from the source to the target, safe means that it
        cannot pass through any vertex that has a camera or any edge that has a toll
        Time complexity:O(E*log V) where E is the total number of edges and V is the total number of vertices
        Space complexity:O(E + V) where E is the total number of edges and V is the total number of vertices
        Error handle: None
        Return: The actual path and the
        Parameter:  source- the vertex where we want to being our shortest path problem from
                    target- the vertes where we want the shortest path problem to finish
        Precondition:source must be an integer
                    target must be an integer
        """
        self.resetVertices()
        finalised = []
        discovered = []
        discovered.append(self.vertex_list[source])
        self.vertex_list[source].distance = 0
        self.vertex_list[source].discovered = True
        if self.vertex_list[source].camera == True:
            return (None,-1)
        while len(discovered) != 0:
            M = MinHeap(discovered)
            v = M.pop()
            v.discovered = True
            if v.camera == False:
                edge_list = v.edge_list
                for i in range(len(edge_list)):
                    cur_edge = edge_list[i]
                    if cur_edge.toll == False:
                        u = cur_edge.u
                        w = cur_edge.w
                        if u.discovered == False and u.finalised == False:
                            discovered.append(u)
                            u.distance = v.distance + w
                            u.connection = v
                            u.discovered = True
                        elif u.distance > v.distance + w:
                            u.distance = v.distance + w
                            u.connection = v
                finalised.append(v)
                discovered.remove(v)
                v.finalised = True
            else:
                discovered.remove(v)

        time = 0
        validpath = False
        for i in finalised:
            if i.id == target:
                time = i.distance
                validpath = True
        #print(finalised)
        if len(finalised) == 1:
            return ((None, -1))
        reversedPath = []
        current = self.vertex_list[target]
        reversedPath.append(current.id)
        while current.id != source:
            reversedPath.append(current.connection.id)
            current = current.connection
        path = []
        for i in range(len(reversedPath) - 1, -1, -1):
            path.append(reversedPath[i])

        string = ""
        for i in range(len(path)):
            string += str(path[i])
            if i < len(path) - 1:
                string += " -> "
        if validpath == True:
            return ((string, time))
        elif validpath == False:
            return ((None, -1))

    def addServices(self,servicefilename):
        """
        Functionality of the function: adds services into the graph
        Time complexity: O(S) where S is the number of services
        Space complexity: O(S) where S is the number of services
        Error handle: None
        Return: None
        Parameter: servicefilename is the name of the file containing all the services
        Precondition: servicefilename should be a string
        """
        with open(servicefilename) as service_file:
            services_list = service_file.read().splitlines()
        #print(services_list)
        for i in services_list:
            self.vertex_list[int(i)].service = True
            self.service_list.append(self.vertex_list[int(i)])
        #print(self.service_list)

    def quickestDetourPath(self,source,target):
        """
        Functionality of the function: find the quickest detour path from the source to the target, detour means that it
        must pass through atleast one service
        Time complexity:O(E*log V) where E is the total number of edges and V is the total number of vertices
        Space complexity:O(E + V) where E is the total number of edges and V is the total number of vertices
        Error handle: None
        Return: The actual path and the
        Parameter:  source- the vertex where we want to being our shortest path problem from
                    target- the vertes where we want the shortest path problem to finish
        Precondition:source must be an integer
                    target must be an integer
        """
        self.resetVertices()

        sourceIsService = False
        for i in self.service_list:
            if i.id == source:
                sourceIsService = True

        if sourceIsService == True:
            return (self.quickestPath(source,target))

        self.resetVertices()
        if source == target:
            if source in self.service_list:
                return ((str(source),'0'))
            else:
                return (None,-1)

        finalised = []
        discovered = []
        discovered.append(self.vertex_list[source])
        self.vertex_list[source].distance = 0
        self.vertex_list[source].discovered = True
        while len(discovered) != 0:
            M = MinHeap(discovered)
            v = M.pop()
            v.discovered = True
            edge_list = v.edge_list
            for i in range(len(edge_list)):
                cur_edge = edge_list[i]
                u = cur_edge.u
                w = cur_edge.w
                if u.discovered == False and u.finalised == False:
                    discovered.append(u)
                    u.distance = v.distance + w
                    u.connection = v
                    u.discovered = True
                elif u.distance > v.distance + w:
                    u.distance = v.distance + w
                    u.connection = v
            finalised.append(v)
            v.finalised = True
            discovered.remove(v)



        reverseFileList = []
        fileList = self.buildList
        for i in fileList:
            j = i.split()
            reverseFileList.append(j)
        for i in reverseFileList:
            i[0],i[1] = i[1],i[0]

        old_vertex_list = self.vertex_list

        self.resetGraph()

        vertixList = []
        for i in range(len(reverseFileList)):
            if reverseFileList[i][0] not in vertixList:
                vertixList.append(reverseFileList[i][0])
            if reverseFileList[i][1] not in vertixList:
                vertixList.append(reverseFileList[i][1])

        self.no_vertices = len(vertixList)
        self.vertex_list = [None] * self.no_vertices
        for i in range(len(vertixList)):
            self.new_vertex(int(vertixList[i]))

        for i in reverseFileList:
            point1 = int(i[0])
            point2 = int(i[1])
            weight = float(i[2])
            self.new_edge(point1, self.vertex_list[point2], weight)

        for i in self.service_list:
            self.vertex_list[int(i.id)].service = True

        self.resetVertices()

        finalised = []
        discovered = []
        discovered.append(self.vertex_list[target])
        self.vertex_list[target].distance = 0
        self.vertex_list[target].discovered = True

        while len(discovered) != 0:
            M = MinHeap(discovered)
            v = M.pop()
            v.discovered = True
            edge_list = v.edge_list
            for i in range(len(edge_list)):
                cur_edge = edge_list[i]
                u = cur_edge.u
                w = cur_edge.w
                if u.discovered == False and u.finalised == False:
                    discovered.append(u)
                    u.distance = v.distance + w
                    u.connection = v
                    u.discovered = True
                elif u.distance > v.distance + w:
                    u.distance = v.distance + w
                    u.connection = v
            finalised.append(v)
            v.finalised = True
            discovered.remove(v)

        TotalPath = []
        for i in finalised:
            if i.service == True:
                TotalPath.append(i)
        for i in TotalPath:
            i.distance += old_vertex_list[i.id].distance

        if TotalPath == []:
            return (None,-1)

        min_service = TotalPath[0]
        for i in TotalPath:
            if i.distance < min_service.distance:
                min_service = i


        finalTime = min_service.distance
        reversedPath = []
        current = min_service
        reversedPath.append(current.id)
        while current.id != target:
            reversedPath.append(current.connection.id)
            current = current.connection
        string = ""
        for i in range(1,len(reversedPath)):
            string += str(reversedPath[i])
            if i < len(reversedPath) - 1:
                string += " -> "
        path2 = string
        #print(path2)

        self.resetGraph()
        self.buildGraph(self.filename)
        self.resetVertices()

        finalised = []
        discovered = []
        discovered.append(self.vertex_list[source])
        self.vertex_list[source].distance = 0
        while len(discovered) != 0:
            M = MinHeap(discovered)
            v = M.pop()
            v.discovered = True
            edge_list = v.edge_list
            for i in range(len(edge_list)):
                cur_edge = edge_list[i]
                u = cur_edge.u
                w = cur_edge.w
                if u.discovered == False and u.finalised == False:
                    discovered.append(u)
                    u.distance = v.distance + w
                    u.connection = v
                    u.discovered = True
                elif u.distance > v.distance + w:
                    u.distance = v.distance + w
                    u.connection = v
            finalised.append(v)
            v.finalised = True
            discovered.remove(v)

        a_node = None
        for i in finalised:
            if i.id == min_service.id:
                a_node = i

        if a_node == None:
            return (None,-1)

        reversedPath = []
        current = a_node
        reversedPath.append(current.id)
        while current.id != source:
            reversedPath.append(current.connection.id)
            current = current.connection
        path = []
        for i in range(len(reversedPath) - 1, -1, -1):
            path.append(reversedPath[i])

        string = ""
        for i in range(len(path)):
            string += str(path[i])
            if i < len(path) - 1:
                string += " -> "
        path1 = (string)
        path1 += " -> "
        CompletePath = (path1 + path2)
        return (CompletePath,finalTime)



if __name__ == "__main__":
    """
    print('---------------------------------------------------------------------')
    graphfilename = input("Enter the file name for the graph : ")
    camerafilename = input('Enter the file name for camera nodes : ')
    tollfilename = input('Enter the file name for the toll roads : ')
    servicefilename = input('Enter the file name for the service nodes : ')
    print('---------------------------------------------------------------------')
    """
    graphfilename = "basicGraph.txt"
    camerafilename = "camera.txt"
    tollfilename = "toll.txt"
    servicefilename = "services.txt"

    source = int(input('Source node: '))
    target = int(input('Sink node: '))
    G = graph()
    G.buildGraph(graphfilename)
    G.augmentGraph(camerafilename,tollfilename)
    quickestPath = G.quickestPath(source,target)
    quickestSafePath = G.quickestSafePath(source,target)
    G.addServices("services.txt")
    quickestDetourPath = G.quickestDetourPath(source,target)
    print('---------------------------------------------------------------------')
    print("Quickest Path:")
    if quickestPath[0] == None:
        print("No Path Exists")
    else:
        print(quickestPath[0])
    print("Time: ",quickestPath[1], "minute(s)")
    print('---------------------------------------------------------------------')
    print("Safe quickest path:")
    if quickestSafePath[0] == None:
        print("No Path Exists")
    else:
        print(quickestSafePath[0])
    print("Time: ", quickestSafePath[1], "minute(s)")
    print('---------------------------------------------------------------------')
    print("Quickest detour path")
    if quickestDetourPath[0] == None:
        print("No Path Exists")
    else:
        print(quickestDetourPath[0])
    print("Time: ", quickestDetourPath[1], "minute(s)")

