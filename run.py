
if __name__ == '__main__': # pragma : no cover
    from equation.BoolTree import Equation
    from solvers.FlipGA import FlipGA
    from solvers.EvoSAP import EvoSAP
    from solvers.BlindGA import BlindGA
    from pprint import PrettyPrinter
    import examples.interpreter as interpreter

    printer = PrettyPrinter(indent=4)   # Setup something which can print dictionaries

    # Get experimental class
    from solvers.experimental.FlipGA import FlipGA_1, FlipGA_2, FlipGA_3

    # Setup variable to hold results
    results = []

    # Test
    cnt = 0
    while cnt <= 25:  # For each data set
        i = 0
        contents = interpreter.interpret_file("examples/data/CBS_k3_n100_m449_b70_" + str(cnt) + ".cnf")
        equation_string = contents[0]
        variables = contents[1]
        print("Generating Equation")
        eq = Equation(equation_string)
        res = []
        av_res = {
            'Test Case': "CBS_k3_n100_m449_b70_" + str(cnt) + ".cnf",
            'AES': None,
            'SR': None
        }

        while i <= 5:   # Do it 5 times
            print("Instantiating Algorithm (FlipGA_1)")
            ga = FlipGA_1(eq, variables)
            ga.run()

            # Output
            trial_res = {'aes': ga._eval_count, 'solved': False} # Trial results
            if ga.generation < 5000:
                trial_res['solved'] = True
            res.append(trial_res)
            i = i + 1
        
        # Calculate test set results
        for r in res:
            if av_res['AES'] is not None:   # AES
                av_res['AES'] = av_res['AES'] + r['aes']
            else:
                av_res['AES'] = r['aes']           
            if av_res['SR'] is not None:    # SR
                if r['solved']:
                    av_res['SR'] = av_res['SR'] + 1
            else:
                if r['solved']:
                    av_res['SR'] = 1
        # Averages
        av_res['AES'] = av_res['AES'] / i
        av_res['SR'] = av_res['SR'] / i
        results.append(av_res)

        # Output
        print("FINISHED TRAINING SET: examples/data/CBS_k3_n100_m449_b70_" + str(cnt) + ".cnf")
        printer.pprint(av_res)

        cnt = cnt + 1
    
    # Output results
    for r in results:
        print("{}\t{}\t{}".format(r['Test Case'], r['AES'], r['SR']))