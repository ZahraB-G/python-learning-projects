# Calculate Simple Interest (SI) using the formula:
#Where: P = Principal amount, T = Time (in years), 
# R = Rate of interest (per annum) Your function 
# should enforce keyword-only arguments 
def simple_interest(*,principle:float, time_year, interest) -> float:
    return (principle * time_year * interest)/100

print(simple_interest(principle=100, time_year=2, interest=10))