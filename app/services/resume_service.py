def generate_resume(data):

    resume = f"""
====================================
{data.name.upper()}
====================================

Email : {data.email}
Phone : {data.phone}

------------------------------------
EDUCATION
------------------------------------

{data.education}

------------------------------------
SKILLS
------------------------------------

{data.skills}

------------------------------------
PROFESSIONAL SUMMARY
------------------------------------

{data.name} is a motivated student with
a strong interest in technology,
continuous learning and innovation.

====================================
"""

    return resume