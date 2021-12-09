# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    #opening_brackets_stack = []
    stack =  []
    for i in range(len(text)):
    #for i, next in enumerate(text):
        if text[i] in "([{":
        #if next in "([{":
            # Process opening bracket, write your code here
            bracket = Bracket(text[i],i)
            stack.append(bracket)
            #pass

        #if next in ")]}":
        if text[i] in ")]}":    
            # Process closing bracket, write your code here
            if len(stack)==0:
                return i+1
            last = stack[-1].char
            #if are_matching(last,next):
            if are_matching(last,text[i]):
                stack.pop(-1)
            else:
                return i+1
            #pass
    if len(stack) != 0:
        return stack[-1].position + 1 
    else:
        return 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()


'''


#print(are_matching('{','}'))
#print(are_matching('[','}'))
#print(are_matching('a','}'))
for s in ['[]','{}[]','[()]','(())','{[]}()','{','{[}','foo(bar)','foo(bar[i)']:
    print(find_mismatch(s))


#for i, next in enumerate('([{[[([(({[{({{{({{{{(({[([([({{[({{[{[[{{[([(([([[{{{{{{({[[[[[(({[[[([[{[[[[([((([[({{[{(({[(([[[[([[{({{{({{{(({[[(([({{{{{{[{([[{[[{{{[{{{(([([{[([({{[[[{[[({([{{{{{(({((([[({((({[{{[([{{{{((({[({[{([[[([{{{{[[{({(([([([([[[(((([[[[[{(([{[((({[([{(([[{([[[((({{({{{[({{([({({[[[[{{({({(({[[[[(([([{(((((({[{[([{([({{{({([[({({{[((({{[[{[{[{[({([([((([[[{({[[([[({[([([({[[{(([{[[([({[[([([[[[[{{{(([[{[[[[[([([{((({(({{{{[(({({[{({[{[([[{([({((([[[[(({({{[[{[({{{({[{{(([{[{(([{[({[[[{[(([({{{({[(((([{[{[({[[[[[({[{((([{{[((({[{[{[[{{[({{[{[[[(([([[{[[({{(({[[{([{[([{([({{[([[({[{[[[[[{[(((([[([[[((({((({({{([(({{({((({({{(([[([[(([(([({[(([[([[{{{([([({([[{[([[{{[[({{{[{{(((((([{(({{[[([[{[{{[([[[[[({(({([{{{{(([{[({[{[{{({[{{[[(({([[(([([{{{{{([[[{[[[[(({{{({{{{[(([{(({{{[[{{(({[{[((([[[{[[{[{(({{[{{({{{{[{{(((([[[([(([([([({(([{{{([{(([[{({[{[{[[({({{([{[{{(({[{([{[{[{(([({([{[{{(({([[(((([([{[{([{[([({{[{[((({{({{[[[[(((([[({[{([(([{([{{{[({([{{[[({[{[{{([[(([{{({[(([[{([[({(([[({{(({({([(({[({{[{[[[[[[{{([({[(([({({[{{([{{({({{{([[[[[{({[{({[{{[[[{{{({(([(([{{{[([(({[{({[{[({{({{[((({{{{(({[{{{{{{(({[[[[({({(({([([({{([[{[{([{{[{{[((({([[{([{[[({[{{[[({{{{([[([{([{([([{{((([[[(([{{([{(([[((([([[([({[[{[{(((({(({((((((([[{({({{{[{[((([((([({({([{{[([([[[{[{({[{[[{{({[{[{((({({(([{({({[([[{{[([{([([{([((({([(([{[([[({((({[[({[(({(((([[({([(((([({{(([[([{[((([{[[[(([{[{[{[([{[({{[([[(({({[[([[((({[[((([([{{([{(([{[[[(({(({[(((([{([(({[([(([({({({{({([(([(([({{[[[{[[{{([([[[{({[{{[({[({{[{{{{[({({[[{{({[[{(([(((({{[{([{(([[[{[([[{(({(({[[[[[({[[({({{[({({[[{{({[([[([[[[{([{{{[{{([[{([[((([[{({{[({({{{({[{({{({((([[{[[{({{[{((([{({([[{{{[((({[(({{([{{[{[{{[{[[({(({([[{[[{({({{{[(([{{[[({{{{[{{(([((({{{{{({[[{[([[{({[[([[({{((({([{(([[[[{{[({[{[([[{([(([((([{[[{([((([[{{[([[[[[({[{({({{[[{{({[([{{[([[[{[{([([{({({{{(([{{[[{[[({[({({[[([{[{{{({(({[{{[{([((((({{{[[{({{{(({{{[[([[{[{[[[[({([{(({({(({({({([[(([[{[(([([{[(([{[{[{{[{{[{{{({(({[({{[{[[[[{([([[({{[({{([[(({{{(((({[{([([{[(([[[[[{{({[{[[[([{[[[{[{([[(([[{{(({{{{(([({([[(([{(((([([{({([[[[[{[({{[[[{{({([((({{[[(([{{([{[({(([[{[(({[{{[({{{[({[[[{{{[[{({({{[{{({{[({([[([{{{[({(({{(({[[{[([{((({[{(({({[((([([([([({([{([{([{(({[{{([{[{([{({[({[(({((({(([[{[(([[([{[{([({[{([{{((({(({([{({[((({([{(({{{{{[(({[{{([{(({[((([({[[[(([{{([({{{{[(([(({(([({{{{[{[{(({[[{{{{{(([[[({{([[[({([{{([{([[(([([ ... }}}})]))}))]))]}}}})])}}]))]]]})])))]}))}])}}]}))]}}}}}))}])})))]})}])}))})))}}])}]})])}]}])]]))]}]]))})))}))]})]})}])}]}])}}]}))}])}])}])})])])])])))]})}))}]})))}])]}]]}))}}))})]}}}])]])})]}})}}]}})})}]]}}}]]]})]}}})]}}]}))]}]]))})]}])}}]))]]}})))])})}}]]]}})]}]]]]])})}])]))))}]))]])})]))}}}}))}}]]))]])}]}]]]}])]]]}]})}}]]]]]))]}])])}]}))))}}}))]])}})]}})]])])}]]]]}]}})]}))})}}}]}}]}}]}]}]))]}])]))]}]]))]])})})}))})}))}])})]]]]}]}]])]]}}}))}}})}]]}}})))))])}]}}]}))})}}}]}])]]})})]})]]}]]}}]))}}})})}])])}]}]]])]}}])]})}}]]}})})}]})]]]]])]}}]])))])}]]}])))]))])}]])]}]})]}}]]]]))}])})))}})]])]]})}]])]}]]})}}}}})))]))}}]}}}})]]}}]))]}}})})}]]}]])}))})]]}]}}]}]}}])}}))]})))]}}}]])})}])))}]}})}]]}]])))})}})}]})}}})})]}})}]])))]])}]])}}]}}}])}]]]])]])]})}}]]})})]}})})]]})]]]]]}))}))}]])]}]]]))}])}]}}))))]))}]]})}}]]})})]}}}}]}})]})]}}]})}]]])])}}]]}]]]}})]))]))])})}})})})]))])]}))])}]))))]}))}))]]]}]))}])}}])])))]]})))]])]]})}))]])]}})]}])]}]}]}]))]]]}])))]}])]]))}})]))))])})]]))))}))]})]]})))})]])]}]))])})))])}])])}])]}}]])]})})}]))})})))}]}]})}}]]}]})}]}]]])])]}}])})})])))])))]}]}}})})}]])))))))}))}))))}]}]]})])]])])))]]))}])}}]))]]])))}}])])}])}])]])}}}})]]}}]})]]}])}]])})))]}}]}}])}]}]])}})])])}))})})]]]]}))}}}}}}]}))}}}})))]}})}})]}]})}]}))])]}}}]))]))})}}}]]]}}]})}]})}]]]]])}}})})}}])}}]})})]))]})])}}]]]]]]}]}})]}))])})}))}})]]))})]])}]]))]})}}]))]])}}]}]})]]}}])})]}}}])}]))])}]})]]))))]]]]}})}})))]}]}})])]}])}]}])]))))]])}))}}]}])})]))}]}]}])}]}))}}]}])}})})]]}]}]})}]]))}])}}}]))})])])]))])]]]))))}}]}}}})}}]}}))}]}]]}]]])))]}]}))}}]]}}}))}]))]}}}})}}}))]]]]}]]])}}}}}])]))]])}))]]}}]})}}]}]})]}]))}}}}])}))})]]]]])]}}]}]])]]}}))}]))))))}}]}}})]]}}]])]}]])})])])}}}]])]]))]})]))]))]])]]))}})})))})}}))])}})})))})))]]])]]))))]}]]]]]}]})]])]}})])}])]}])}]]}))}})]]}]])]))]]]}]}})]}}]]}]}]})))]}}])))}]})]]]]]})]}]}]))))]})}}})]))]}]]]})]}]))}]}]))}}]})}}})]}]]}})}))]]]])))})])}]])]}]})}]})}))]}}}}))})))}])])]]]]]}]]))}}}]]]]])])]]})])]]}]))}]]})])])]})]])]]})}]]])))])])})]}]}]}]]}})))]}})})]])})}}})])}])]}]}))))))}])]))]]]]}))})})}}]]]]})})])}})]}}})}})))]]])}]]))}])]})))]}]))}]]]]]))))]]])])])]))})}]]}}}}])]]])}]})]})))}}}}])]}}]})))})]])))}))}}}}}])})]]}]]]}})])]}])]))}}}]}}}]]}]])}]}}}}}})]))]]}))}}})}}})}]])]]]]))]}))}]}})]])))])]]]]}]])]]]}))]]]]]})}}}}}}]])]))])]}}]]}]}})]}})])])]}))}}}})}}})}]}))])]]}])
#'):
    #print(i)
    #print(next)
mismatch = find_mismatch('([{[[([(({[{({{{({{{{(({[([([({{[({{[{[[{{[([(([([[{{{{{{({[[[[[(({[[[([[{[[[[([((([[({{[{(({[(([[[[([[{({{{({{{(({[[(([({{{{{{[{([[{[[{{{[{{{(([([{[([({{[[[{[[({([{{{{{(({((([[({((({[{{[([{{{{((({[({[{([[[([{{{{[[{({(([([([([[[(((([[[[[{(([{[((({[([{(([[{([[[((({{({{{[({{([({({[[[[{{({({(({[[[[(([([{(((((({[{[([{([({{{({([[({({{[((({{[[{[{[{[({([([((([[[{({[[([[({[([([({[[{(([{[[([({[[([([[[[[{{{(([[{[[[[[([([{((({(({{{{[(({({[{({[{[([[{([({((([[[[(({({{[[{[({{{({[{{(([{[{(([{[({[[[{[(([({{{({[(((([{[{[({[[[[[({[{((([{{[((({[{[{[[{{[({{[{[[[(([([[{[[({{(({[[{([{[([{([({{[([[({[{[[[[[{[(((([[([[[((({((({({{([(({{({((({({{(([[([[(([(([({[(([[([[{{{([([({([[{[([[{{[[({{{[{{(((((([{(({{[[([[{[{{[([[[[[({(({([{{{{(([{[({[{[{{({[{{[[(({([[(([([{{{{{([[[{[[[[(({{{({{{{[(([{(({{{[[{{(({[{[((([[[{[[{[{(({{[{{({{{{[{{(((([[[([(([([([({(([{{{([{(([[{({[{[{[[({({{([{[{{(({[{([{[{[{(([({([{[{{(({([[(((([([{[{([{[([({{[{[((({{({{[[[[(((([[({[{([(([{([{{{[({([{{[[({[{[{{([[(([{{({[(([[{([[({(([[({{(({({([(({[({{[{[[[[[[{{([({[(([({({[{{([{{({({{{([[[[[{({[{({[{{[[[{{{({(([(([{{{[([(({[{({[{[({{({{[((({{{{(({[{{{{{{(({[[[[({({(({([([({{([[{[{([{{[{{[((({([[{([{[[({[{{[[({{{{([[([{([{([([{{((([[[(([{{([{(([[((([([[([({[[{[{(((({(({((((((([[{({({{{[{[((([((([({({([{{[([([[[{[{({[{[[{{({[{[{((({({(([{({({[([[{{[([{([([{([((({([(([{[([[({((({[[({[(({(((([[({([(((([({{(([[([{[((([{[[[(([{[{[{[([{[({{[([[(({({[[([[((({[[((([([{{([{(([{[[[(({(({[(((([{([(({[([(([({({({{({([(([(([({{[[[{[[{{([([[[{({[{{[({[({{[{{{{[({({[[{{({[[{(([(((({{[{([{(([[[{[([[{(({(({[[[[[({[[({({{[({({[[{{({[([[([[[[{([{{{[{{([[{([[((([[{({{[({({{{({[{({{({((([[{[[{({{[{((([{({([[{{{[((({[(({{([{{[{[{{[{[[({(({([[{[[{({({{{[(([{{[[({{{{[{{(([((({{{{{({[[{[([[{({[[([[({{((({([{(([[[[{{[({[{[([[{([(([((([{[[{([((([[{{[([[[[[({[{({({{[[{{({[([{{[([[[{[{([([{({({{{(([{{[[{[[({[({({[[([{[{{{({(({[{{[{([((((({{{[[{({{{(({{{[[([[{[{[[[[({([{(({({(({({({([[(([[{[(([([{[(([{[{[{{[{{[{{{({(({[({{[{[[[[{([([[({{[({{([[(({{{(((({[{([([{[(([[[[[{{({[{[[[([{[[[{[{([[(([[{{(({{{{(([({([[(([{(((([([{({([[[[[{[({{[[[{{({([((({{[[(([{{([{[({(([[{[(({[{{[({{{[({[[[{{{[[{({({{[{{({{[({([[([{{{[({(({{(({[[{[([{((({[{(({({[((([([([([({([{([{([{(({[{{([{[{([{({[({[(({((({(([[{[(([[([{[{([({[{([{{((({(({([{({[((({([{(({{{{{[(({[{{([{(({[((([({[[[(([{{([({{{{[(([(({(([({{{{[{[{(({[[{{{{{(([[[({{([[[({([{{([{([[(([([ ... }}}})]))}))]))]}}}})])}}]))]]]})])))]}))}])}}]}))]}}}}}))}])})))]})}])}))})))}}])}]})])}]}])]]))]}]]))})))}))]})]})}])}]}])}}]}))}])}])}])})])])])])))]})}))}]})))}])]}]]}))}}))})]}}}])]])})]}})}}]}})})}]]}}}]]]})]}}})]}}]}))]}]]))})]}])}}]))]]}})))])})}}]]]}})]}]]]]])})}])]))))}]))]])})]))}}}}))}}]]))]])}]}]]]}])]]]}]})}}]]]]]))]}])])}]}))))}}}))]])}})]}})]])])}]]]]}]}})]}))})}}}]}}]}}]}]}]))]}])]))]}]]))]])})})}))})}))}])})]]]]}]}]])]]}}}))}}})}]]}}})))))])}]}}]}))})}}}]}])]]})})]})]]}]]}}]))}}})})}])])}]}]]])]}}])]})}}]]}})})}]})]]]]])]}}]])))])}]]}])))]))])}]])]}]})]}}]]]]))}])})))}})]])]]})}]])]}]]})}}}}})))]))}}]}}}})]]}}]))]}}})})}]]}]])}))})]]}]}}]}]}}])}}))]})))]}}}]])})}])))}]}})}]]}]])))})}})}]})}}})})]}})}]])))]])}]])}}]}}}])}]]]])]])]})}}]]})})]}})})]]})]]]]]}))}))}]])]}]]]))}])}]}}))))]))}]]})}}]]})})]}}}}]}})]})]}}]})}]]])])}}]]}]]]}})]))]))])})}})})})]))])]}))])}]))))]}))}))]]]}]))}])}}])])))]]})))]])]]})}))]])]}})]}])]}]}]}]))]]]}])))]}])]]))}})]))))])})]]))))}))]})]]})))})]])]}]))])})))])}])])}])]}}]])]})})}]))})})))}]}]})}}]]}]})}]}]]])])]}}])})})])))])))]}]}}})})}]])))))))}))}))))}]}]]})])]])])))]]))}])}}]))]]])))}}])])}])}])]])}}}})]]}}]})]]}])}]])})))]}}]}}])}]}]])}})])])}))})})]]]]}))}}}}}}]}))}}}})))]}})}})]}]})}]}))])]}}}]))]))})}}}]]]}}]})}]})}]]]]])}}})})}}])}}]})})]))]})])}}]]]]]]}]}})]}))])})}))}})]]))})]])}]]))]})}}]))]])}}]}]})]]}}])})]}}}])}]))])}]})]]))))]]]]}})}})))]}]}})])]}])}]}])]))))]])}))}}]}])})]))}]}]}])}]}))}}]}])}})})]]}]}]})}]]))}])}}}]))})])])]))])]]]))))}}]}}}})}}]}}))}]}]]}]]])))]}]}))}}]]}}}))}]))]}}}})}}}))]]]]}]]])}}}}}])]))]])}))]]}}]})}}]}]})]}]))}}}}])}))})]]]]])]}}]}]])]]}}))}]))))))}}]}}})]]}}]])]}]])})])])}}}]])]]))]})]))]))]])]]))}})})))})}}))])}})})))})))]]])]]))))]}]]]]]}]})]])]}})])}])]}])}]]}))}})]]}]])]))]]]}]}})]}}]]}]}]})))]}}])))}]})]]]]]})]}]}]))))]})}}})]))]}]]]})]}]))}]}]))}}]})}}})]}]]}})}))]]]])))})])}]])]}]})}]})}))]}}}}))})))}])])]]]]]}]]))}}}]]]]])])]]})])]]}]))}]]})])])]})]])]]})}]]])))])])})]}]}]}]]}})))]}})})]])})}}})])}])]}]}))))))}])]))]]]]}))})})}}]]]]})})])}})]}}})}})))]]])}]]))}])]})))]}]))}]]]]]))))]]])])])]))})}]]}}}}])]]])}]})]})))}}}}])]}}]})))})]])))}))}}}}}])})]]}]]]}})])]}])]))}}}]}}}]]}]])}]}}}}}})]))]]}))}}})}}})}]])]]]]))]}))}]}})]])))])]]]]}]])]]]}))]]]]]})}}}}}}]])]))])]}}]]}]}})]}})])])]}))}}}})}}})}]}))])]]}])
')
print(mismatch)
'''