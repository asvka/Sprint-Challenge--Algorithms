#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

 a: O(n^2) or O(n^3) maybe -- multiplying each time during iteration

b)

b: O(n^2) -- Nested loop within a loop.

c)

c: O(n) -- at first I assumed this was O(1), but it's actually O(n) as it's recursively calling bunnyEars

## Exercise II

def egg_drop(e, f, n):
    eggs_destroyed = e
    floor = n
    breaking_point_floor = f
    
    while floor < breaking_floor:
        floor += 1
        eggs_destroyed == 0
    
        if floor == breaking_point_floor:
            eggs_destroyed += 1
            return floor
    
    
#Sorry, I know this is pretty sloppy. But here's the basic idea that I have:
Basically we'll go up a floor each time we get to a floor that doesn't break an egg.
If the floor reaches the breaking point, we add to our count of broken eggs.
We then return the floor that it broke on.
I believe this is O(n^2) as we're once again nesting loops within loops.
I'm sure this could've been written better, but due to time constraints... ta-dahhhh lmao
