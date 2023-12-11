How memory is managed in Python?

Ans:
     According to the Python memory management documentation, Python has a private heap that stores our 
program’s objects and data structures. Python memory manager takes care of the bulk of the memory 
management work and allows us to concentrate on our code.

Garbage Collection:
                  Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for other objects.Assume a case where no reference is pointing to an object in memory i.e. it is not in use so, the virtual machine has a garbage collector that automatically deletes that object from the heap memory

Reference Counting:
                  Reference counting works by counting the number of times an object is referenced by other objects in the system. When references to an object are removed, the reference count for an object is decremented. When the reference count becomes zero, the object is deallocated.

Memory Allocation in Python is two parts of memory:

1.stack memory:
               The allocation happens on contiguous blocks of memory. We call it stack memory allocation because the allocation happens in the function call stack. The size of memory to be allocated is known to the compiler and whenever a function is called, its variables get memory allocated on the stack.

It is the memory that is only needed inside a particular function or method call. When a function is called, it is added onto the program’s call stack. Any local memory assignments such as variable initializations inside the particular functions are stored temporarily on the function call stack, where it is deleted once the function returns, and the call stack moves on to the next task. This allocation onto a contiguous block of memory is handled by the compiler using predefined routines, and developers do not need to worry about it.

Example:
def func(): 

	a = 20
	b = [] 
	c = "" 

2.heap memory:
              The memory is allocated during the execution of instructions written by programmers. Note that the name heap has nothing to do with the heap data structure. It is called heap because it is a pile of memory space available to programmers to allocated and de-allocate. The variables are needed outside of method or function calls or are shared within multiple functions globally are stored in Heap memory.

Example:
         
         a = [0]*10 

