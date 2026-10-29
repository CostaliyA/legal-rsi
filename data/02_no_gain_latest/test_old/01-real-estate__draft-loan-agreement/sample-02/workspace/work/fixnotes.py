# Post-processing: normalize every Drafting Note cross-reference to the Cover Memorandum issue numbers.
import re, docx

MAP = {
 'Section 2.1  The Commitment': '19',
 'Section 2.10  Fees': '19',
 'Section 2.14  Extension Option': '13',
 'Section 2.16  Maximum Rate; Usury Savings': None,
 'Section 3.4  Survey': '7',
 'Section 3.5  Environmental Conditions': '8 and 11',
 'Section 3.6  Historic District Covenant Compliance': '9',
 'Section 3.7  Equity Contribution and Sources and Uses': '3',
 'Section 3.9  Single-Purpose Entity Amendments; Non-Consolidation Opinion': '15',
 'Section 3.11  Construction Documents': '5',
 'Section 3.14  Payoff and Release of Prior Deed of Trust': '2',
 'Section 3.15  Lien Waivers and No Prior Work': '10',
 'Section 3.16  Financial Information': '14',
 'Section 4.1  Draw Schedule': '5',
 'Section 4.6  Equity First; Cost Overruns': '1',
 'Section 5.6  Interest Reserve Analysis; Acknowledgement': '12',
 'Section 9.1  Loan-to-Cost Ratio': '3',
 'Section 9.2  Loan-to-Value Ratios': '4',
 'Section 9.3  Debt Service Coverage Ratio': '13',
 'Section 9.4  Borrower Net Worth': '14',
 'Section 11.3  Partial Repayment Guaranty': '16',
 'Section 11.5  Environmental Indemnity': '16',
 'Section 11.8  North Carolina Deficiency and Fair Value Matters': '21',
 'Section 13.16  Invalidity of Environmental Compliance': '19',
 'Section 16.2  Mini-Perm Period Coverage': '18',
 'SCHEDULE 1 \u2014 DRAW SCHEDULE AND CONSTRUCTION MILESTONES': '5',
 'SCHEDULE 2 \u2014 PROJECT BUDGET AND SOURCES AND USES OF FUNDS': '1, 2 and 3',
 'SCHEDULE 3 \u2014 PERMITTED EXCEPTIONS': '20',
 'EXHIBIT A \u2014 LEGAL DESCRIPTION': '7',
}

def normalize(path):
    d = docx.Document(path)
    cur = None
    changes = []
    for p in d.paragraphs:
        st = p.style.name if p.style is not None else ''
        if st in ('Heading 1', 'Heading 2') and p.text.strip():
            cur = p.text.strip()
        if 'Drafting Note' in p.text and cur in MAP and MAP[cur]:
            new = MAP[cur]
            for r in p.runs:
                if 'Cover Memorandum Issue' in r.text:
                    r.text = re.sub(r'(Cover Memorandum Issue(?:s)? No(?:s)?\. )(\d[\d,]*(?: and \d+)?)',
                                    lambda m: m.group(1) + new, r.text)
                    changes.append((cur, new))
    d.save(path)
    return changes

if __name__ == '__main__':
    for c in normalize('/workspace/output/loan-agreement-draft.docx'):
        print(c)
