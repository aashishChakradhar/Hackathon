import random

coding_question = {
    "You are tasked with improving the performance of a function that processes a large dataset. The function is slow due to repeated operations and inefficient data structures. Which of the following strategies would help optimize the function?" :{
        0 : "Switch from a list to a linked list for faster random access.",
        1 : "Use recursion to reduce the amount of code and improve performance by avoiding loops.",
        2 : "Avoid premature optimization and focus on code readability and maintainability, as the function might be fast enough for most use cases.",
        3 : "Profile the code using a performance profiling tool to identify the slowest parts of the function and focus optimization efforts there.",
        4 : "Replace nested loops with a hash map (dictionary in Python) where possible to reduce the time complexity of lookups.",
        5 : "Implement caching (memoization) to store results of expensive function calls and avoid redundant computations.",
    },
    "You are developing an application that processes user input and stores it in a database. To ensure the application is robust and efficient, which strategies would you implement for handling user input and database interactions? " : {
        0 : "Log all user inputs without any restrictions for debugging purposes.",
        1 : "Use raw SQL queries for all database interactions to maximize performance.",
        2 : "Sanitize user input before storing it in the database to prevent security vulnerabilities.",
        3 : "Utilize connection pooling to manage database connections efficiently and reduce latency.",
        4 : "Validate user input on both the client side and server side to prevent invalid data from being processed.",
        5 : "Implement prepared statements or parameterized queries to protect against SQL injection attacks.",
    },
    "You are developing a mobile application that needs to handle real-time user location updates efficiently. What strategies would you implement to ensure optimal performance and resource usage?" : {
        0 : "Continuously request the most accurate location data every second to ensure precision at all times.",
        1 : "Send all location updates to the server immediately, regardless of their frequency or the user’s activity state.",
        2 : "Implement background location updates with minimal accuracy to save power when the user is not actively using the app.",
        3 : "Utilize a low-power location tracking API that reduces the frequency of location updates while maintaining acceptable accuracy.",
        4 : "Optimize the data processing of location updates by using efficient algorithms to handle and store data.",
        5 : "Use geofencing to limit location updates to specific areas, reducing unnecessary computations and battery usage.",
    },
    "You are tasked with improving the performance of a function that processes a large dataset. The function is slow due to repeated operations and inefficient data structures. Which of the following strategies would help optimize the function?" : {
        0 : "Switch from a list to a linked list for faster random access.",
        1 : "Use recursion to reduce the amount of code and improve performance by avoiding loops.",
        2 : "Avoid premature optimization and focus on code readability and maintainability, as the function might be fast enough for most use cases.",
        3 : "Profile the code using a performance profiling tool to identify the slowest parts of the function and focus optimization efforts there.",
        4 : "Implement caching (memoization) to store results of expensive function calls and avoid redundant computations.",
        5 : "Replace nested loops with a hash map (dictionary in Python) where possible to reduce the time complexity of lookups.",
    },
    "You are developing an application that needs to handle a large number of user requests efficiently. What techniques would you use to ensure the application scales well under high load?" : {
        0 : "Write code that is easy to read and maintain, as it will help future developers.",
        1 : "Use a single-threaded event loop to handle requests asynchronously.",
        2 : "Implement rate limiting to control the number of requests a user can make in a given time frame.",
        3 : "Use microservices architecture to break down the application into smaller, manageable services.",
        4 : "Implement load balancing to distribute incoming requests across multiple servers.",
        5 : "Optimize database queries by using indexing and caching frequently accessed data.",
    },
}

leadership_question = {
    'You are leading a team working on a high-pressure project with tight deadlines. Your team members are facing challenges, and the project has fallen behind schedule. How would you handle the situation?' : {
        0 : "Blame the delays on poor performance and demand faster results.",
        1 : "Offer incentives or rewards to motivate the team to meet the deadline.",
        2 : "Take on more work yourself to help reduce the load on your team members.",
        3 : "Delegate tasks to the most capable team members, ensuring the best-qualified people handle the most important work.",
        4 : "Schedule one-on-one meetings with each team member to understand their concerns and offer support.",
        5 : "Hold a team meeting to re-evaluate the timeline, discuss the roadblocks, and reassign tasks if necessary.",
        },
    'You are leading a project team that is facing delays due to poor communication and missed deadlines. As the team leader, how would you approach solving these issues?' : {
        0 : " Assign new tasks to the most productive team members to ensure deadlines are met, even if it means overloading them temporarily.",
        1 : "Delegate all communication responsibilities to one team member to streamline the process and avoid confusion.",
        2 : "Implement a reward system to incentivize the team to meet deadlines and communicate more effectively.", 
        3 : "Privately address team members who are underperforming, giving them feedback on areas for improvement.",
        4 : "Establish clear, structured deadlines and follow-up procedures for all tasks to improve accountability.",
        5 : "Hold a team meeting to identify the communication breakdowns and encourage team members to share their perspectives.",
    },
    'Which of the following actions demonstrate effective leadership in a team setting?' : {
        0 : "You take sole responsibility for project failures and successes, without involving the team in accountability.",
        1 : "You ensure that team conflicts are resolved quickly by imposing a solution, so the team can stay focused on tasks.",
        2 : "You delegate tasks to team members based on their strengths, but you maintain full control over the decision-making process.",
        3 : "You motivate team members by recognizing their efforts and achievements publicly.",
        4 : "You encourage team members to take ownership of tasks, fostering their ability to work independently while providing guidance as needed.",
        5 : "You actively listen to your team's ideas and concerns, incorporating their feedback into project decisions.",
    },
    'You are leading a team that is facing a critical deadline, and two team members are in conflict over how to proceed. As the leader, how would you handle the situation?' : {
        0 : "Make a decision on the best approach yourself and instruct the team to follow it without further discussion.",
        1 : "Call an urgent team meeting to discuss the issue publicly and ask for the team's input. ",
        2 : "Delegate responsibility for resolving the conflict to another senior team member who has more experience with such issues.",
        3 : "Schedule a one-on-one meeting with each team member to understand their perspectives and feelings about the situation.",
        4 : "Encourage both team members to suggest compromises and then help them evaluate the pros and cons of each approach.",
        5 : "Facilitate a discussion between the two team members, helping them to communicate their viewpoints and find common ground.",
    },
    "As a team leader, you are managing a high-pressure project with a tight deadline. Some team members are struggling to keep up, and there's tension in the group. Which of the following actions would demonstrate strong leadership skills? " : {
        0 : "Take full control of the project and personally handle the critical tasks to ensure quality and on-time delivery.",
        1 : "Set strict guidelines and inform the team that failure to meet deadlines will have consequences, ensuring that everyone works harder.",
        2 : "Provide emotional support to struggling team members by having one-on-one conversations to understand their challenges and motivate them.", 
        3 : "Recognize team member's efforts by celebrating small wins and giving praise where due to maintain morale.",
        4 : "Delegate tasks based on each team member's strengths, ensuring that the workload is balanced across the team.",
        5 : "Encourage open communication by holding a team meeting where everyone can voice concerns and suggest improvements.",
    },
}

communication_question = {
    "Imagine you need to explain a complex technical concept (such as APIs) to a non-technical audience. What strategies would you employ to ensure effective communication? " : {
        0 : "Focus on jargon and industry-specific terminology to establish credibility.",
        1 : "Provide a detailed technical explanation, assuming the audience has some prior knowledge.",
        2 : "Summarize the key points at the end to reinforce understanding.",
        3 : "Encourage questions throughout the explanation to gauge understanding.",
        4 : "Use analogies and relatable examples to simplify the concept.",
        5 : "Use visual aids, like diagrams or slides, to complement your explanation.",
    },
    "Imagine you need to explain a complex technical concept (like FastAPI) to a non-technical stakeholder (like a project manager). What strategies would you use to ensure your explanation is clear and effective?" : {
        0 : "Use technical jargon and industry-specific terms to demonstrate expertise.",
        1 : "Assume the stakeholder has a basic understanding of technical concepts and skip introductory explanations.",
        2 : "Create a visual aid, like a diagram or flowchart, to illustrate the concept.",
        3 : "Break down the concept into smaller, more manageable parts, explaining each step clearly.",
        4 : "Encourage questions and be open to clarifying any points that may be confusing.",
        5 : "Provide analogies or real-world examples that relate to the stakeholder's experiences.",
    },
    "Imagine you are leading a team meeting to discuss a new project. How would you effectively communicate your ideas and ensure that all team members are engaged and understand the project's objectives? " : {
        0 : "Use technical jargon and complex terminology to showcase your expertise. ",
        1 : "Speak for the entire duration of the meeting without interruptions to maintain control over the conversation.",
        2 : "Summarize key points and action items at the end of the meeting to ensure everyone is on the same page.",
        3 : "Encourage questions and feedback throughout the meeting to promote discussion.",
        4 : "Use visual aids, such as slides or charts, to help illustrate your points and make the information more digestible.",
        5 : "Clearly outline the project objectives and key deliverables at the beginning of the meeting.",
    },
    "Imagine you need to explain a complex technical concept (such as an algorithm or system architecture) to a non-technical stakeholder. What strategies would you use to ensure your explanation is clear and effective?" : {
        0 : "Use technical jargon to convey expertise and build credibility.",
        1 : "Focus solely on the details to demonstrate thorough knowledge of the topic.",
        2 : "Provide a high-level overview first before diving into details to set the context.",
        3 : "Encourage questions throughout the explanation to clarify any misunderstandings.",
        4 : "Use analogies or metaphors that relate the concept to everyday experiences.",
        5 : "Present the information in a structured format, using bullet points or visuals to aid understanding.",
    },
    "You need to present a complex technical concept to a non-technical audience. How would you approach this presentation?" : {
        0 : "Use technical jargon and in-depth details to showcase your expertise.",
        1 : "Focus on delivering the content as quickly as possible to cover all points.",
        2 : "Encourage questions throughout the presentation to ensure understanding.",
        3 : "Provide a clear overview of the concept before diving into details.",
        4 : "Start with a real-world analogy that relates to the audience’s experiences.",
        5 : "Use visual aids like diagrams or charts to illustrate key points.",
    },
}

presentation_question = {
    "You are tasked with designing a presentation for a diverse audience about a new product. Which of the following strategies would you employ to ensure the presentation is effective?" : {
        0 : "Include as much text as possible to ensure all details are covered.",
        1 : "Structure the presentation with clear headings and bullet points for easy navigation.",
        2 : "Use a consistent color scheme and font style throughout the slides.",
        3 : "Incorporate multimedia elements like videos or animations to engage the audience.",
        4 : "Use high-quality images and graphics to enhance visual appeal.",
        5 : "Keep the slides clutter-free and limit each slide to one main idea.",
    },
    "You are tasked with designing a presentation for a stakeholder meeting to explain a new project. Which of the following design choices would you make to ensure the presentation is effective? " : {
        0 : "Fill slides with detailed text to ensure all information is conveyed.",
        1 : "Include transitions and animations on every slide to make it visually appealing.",
        2 : "Create a summary slide at the end to recap the main points.",
        3 : "Limit the number of slides to keep the presentation concise and focused.",
        4 : "Use a consistent color scheme and font style throughout the slides.",
        5 : "Incorporate high-quality visuals, such as images and graphs, to support key points.",
    },
    "You are tasked with designing a presentation for a key stakeholder meeting. Which strategies would you use to ensure the presentation is effective and engaging? " : {
        0 : "Include as much text as possible to ensure all details are covered.",
        1 : "Choose a variety of fonts and colors to make the slides visually appealing.",
        2 : "Limit the number of slides to keep the presentation concise and focused.",
        3 : "Practice delivering the presentation multiple times to ensure smooth delivery.",
        4 : "Use a consistent and professional template throughout the presentation.",
        5 : "Incorporate visuals such as images, charts, and infographics to support your points.",
    },
    "You are tasked with designing a presentation for an important stakeholder meeting. Which of the following design principles or strategies would you consider?" : {
        0 : "Include as much text as possible to ensure all information is conveyed.",
        1 : "Rely solely on animations and transitions to make the slides more engaging.",
        2 : "Limit the number of slides to keep the presentation concise and focused.",
        3 : "Use high-quality images and graphics to support your points.",
        4 : "Use a consistent color scheme and font throughout the presentation.",
        5 : "Structure the presentation with clear sections and transitions to guide the audience.",
    },
    "You are tasked with creating a presentation for a stakeholder meeting to explain a new product feature. What design elements and strategies would you incorporate to ensure the presentation is effective?" : {
        0 : "Include as much text as possible on each slide to cover all details.",
        1 : "Use animations and transitions on every slide to make it visually dynamic.",
        2 : "Limit the number of slides to keep the presentation concise and focused.",
        3 : "Use a consistent color scheme and font style throughout the presentation.",
        4 : "Provide a clear summary slide at the end to recap key takeaways.",
        5 : "Incorporate visuals such as images, infographics, or charts to support your points.",
    },   
}

def create_random_question_dict():
    new_dict = {}
    dictionaries = [coding_question, leadership_question, communication_question, presentation_question]
    for dictionary in dictionaries:
        random_key = random.choice(list(dictionary.keys()))
        new_dict[random_key] = dictionary[random_key]
    return new_dict

# Example usage:
dictionaries = [coding_question, leadership_question, communication_question, presentation_question]
random_questions = create_random_question_dict()
# print(random_questions)


# Print the key and value
# print(random_question)
# print(random_answer)

    
# def hello():
#     return('Hello world')

# def randomQuestion(skill):
#     questionList = list(skill.keys())
#     random_question = random.choice(questionList)
#     questionDict = {
#         "question" : random_question,
#         "answer" : skill[random_question],
#     }
#     return questionDict

# print(randomQuestion(leadership_question))