def convert_quintiles(country_age, income_country):
    total_pop = sum(country_age["M"]) + sum(country_age["F"])
    bin_size  = round(total_pop / 5)
    
    quintiles_working = {
        "q_income" : [0] * 5,
        "q_people" : [0] * 5,
        "q_male"   : [0] * 5
    }
  
    quintiles = {
        "income_prop" : [],
        "sex_prop"    : []
    },

  
    current_quantile = 0
    current_bin_size = bin_size
    for male, female, income_bracket in zip(country_age["M"], country_age["F"], income_country):
        br_inc  = male + female
        sex_prop = Decimal(male / br_inc)
        
        while br_inc > 0:
            calc = divmod(current_bin_size, br_inc)
            # if the quotient is more than 1 (income bracket fully fills the quantile)
            if calc[0] >= 1:
                quintiles_working["q_income"][current_quantile] += income_bracket * current_bin_size
                quintiles_working["q_people"][current_quantile] += current_bin_size
                quintiles_working["q_male"][current_quantile]   += round(current_bin_size * sex_prop)
                
                # update current_quantile
                current_quantile += 1
                current_bin_size = bin_size
                # keeps remainder + quotient not used up
                br_inc = calc[1] + ((calc[0] - 1) * br_inc)
            
            #quotient is less than 1 (income bracket does not fill the quantile)
            else:
                quintiles_working["q_income"][current_quantile] += income_bracket * br_inc
                quintiles_working["q_people"][current_quantile] += br_inc
                quintiles_working["q_male"][current_quantile]   += round(br_inc * sex_prop)
                current_bin_size -= br_inc
                br_inc = 0
        
    total_income = sum(quintiles_working["q_income"])
    quintiles["income_prop"] = [income / total_income for income in quintiles_working["q_income"]]
    quintiles["sex_prop"]    = [males / people for males, people in zip(quintiles_working["q_male"], quintiles_working["q_people"])]
    
    return quintiles
