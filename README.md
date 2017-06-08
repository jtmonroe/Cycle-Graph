# Cycle_Graph
### Joel Monroe

### The College of William and Mary

File created to assist in Research for the William and Mary EXTREEMS-QED 2017 program. Please use for any projects!

* ## Initiation
* Takes no arguments, but inititalizes a graph system very similar to that of a doubly linked list. 

    * ### Cycle_Graph initialization:
        * Initializes with slots for a base node, a standing node, length, and number of steps. 
            * Base_Node
                Initialized to allow users to enter the graph from a consistent point. Currently set to be the minimum of objects within the list.
                
            * Standing
                Allows for users to make changes to the list depending upon which node they are standing upon. Two nodes cannot be stood upon at once.
            
            * Length and steps
                For the sake of the user's interest.
    
    *  ### __cg_Node initialization:
        * Initializes with slots for prev and next pointers, value, spin, pos.
            * Prev and Next
                Pointers to distinguish the list and next values.
            
            * Val 
                Value that the node holds.
                
            * Spin
                Distance of the Node values from their base position.
                
            * Pos
                The postion of the node with relation to the lowest value.
                
            * N
                the length of the list for purposes of comparison.
                
    * ### __cg_Node __gt__():
        * tests to see if the nodes are comparable, ie; spin(a) - spin(b) > pos(b) - pos(a) (+ n if a > b).
                
* ## Filling the Graph
    
    * ### Input:
        * Takes a list as an arguement and fills the graph using subfunctions. Simultaneously  also sets the base node and the spin and position values of the nodes.
        
        * __insert()
        pushes the new value onto the graph, while retaining the cyclic form. Increments length each time.
        
        
        * __pos_assign()
        assigns positions based on the base node position, which starts at 1.
        
        * __spin_assignment()
        sets the spin as the distance the node must travel so that its position equals its value.
        
* ## len and str functions
    * ### len:
        * returns the total number of nodes in the system.
        
    * ### str
        * returns a line of pointers which direct from node to node, ending and starting with the base node.
        
* ## Graph Properties
    * ### dist()
        * returns a list containing all the spins of the nodes.
        
    * ### total_spin()
        * Returns the sum of the absolute value of the spins.
        
    * ### terms()
        * Returns a list with all terms in original order.
        
    * ### not_ordered()
        * Tests if cycle is unordered. Returns false if not, true if it is unordered.
        
    * ### value(), spin(), and position()
        * Returns the value, spin, and position of the standing node.
        
    * ### next_value() and next_spin() 
        * Returns the value and spin of the node after the standing node.
        
    * ### steps()
        * Returns the total number of steps logged.
        
    * ### compare()
        * Compares the standing node and the next to see if they are comparable.
        
        
* ## Sorting Functions
    * ### optimize()
        * Minimizes the absolute value of the sums of the spins by reducing the value of the maximum and minimum spins if their sum is greater than the length.
        
    * ### step_counter()
        * counts the total number of steps and attaches it as a property to the graph object.
        
    * ### next_node() and prev_node()
        * Allows the user to move to the next node without using a current walk. Utilizes the standing node to move through the graph.
        
    * ### reset()
        * Sets the standing node back to the base node.
        
    * ### swap()
        * Takes in two consectutive nodes and swaps them.
        

