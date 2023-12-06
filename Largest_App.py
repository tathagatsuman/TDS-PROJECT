import streamlit as st

def find_largest_number(a, b, c):
    if a >= b:
        if a >= c:
            largest = a
        else:
            largest = c
    elif b >= a:
        if b >= c:
            largest = b
        else:
            largest = c
    return largest

def main():
    st.title('Find the Largest Number')
    st.write("Enter three numbers and find the largest among them...")
    number1 = st.number_input('Enter the first number: ')
    number2 = st.number_input('Enter the second number: ')
    number3 = st.number_input('Enter the third number: ')
    if st.button('Find Largest Number'):
        largest = find_largest_number(number1, number2, number3)
        st.write(f"The largest number among the three is: {largest}")

if __name__ == "__main__":
    main()
