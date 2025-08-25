def highlight_element(driver, element):
    driver.execute_script("""
        const arg = arguments[0];
        const prev = arg.style.border;       
        arg.style.border = '4px solid yellow';
        setTimeout(() => { arg.style.border = prev; }, 300); 
    """, element)
