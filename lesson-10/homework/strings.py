class Task:
    def __init__(self, title, descripton,due_date):
        self.title=title,
        self.description=descripton,
        self.due_date = due_date,
        self.status= False
    def mark_complite(self):
        self.status = True
    def __str__(self):
        status = "Done" if self.status else "Not Done"
        return f"{self.title} - {status}\n  Description: {self.description}\n  Due: {self.due_date}"

class ToDOlist(Task):
    def __init__(self):
        self.tasks =[]
    def add_task(self, task):
        self.tasks.append(task)
        print(f'Added task: {task}')
    def mark_complited(self, index):
        if 0<=index<len(self.tasks):
            self.status=True
        else:
            print('Invalid task index.')
    def list_all_tasks(self):
        for i, task in enumerate(self.tasks):
            print (f'{i}: {task}')
    def list_imcomplete_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task.status:
                print(f'{i}: {task['task']} - Not Done')
    def __repr__(self):
        return f'Title: {self.title}\nDescription:{self.description}\nDue date: {self.due_date}\nStatus: {self.status}'


def print_menu():
    print('Main menu')
    print('1. Add task')
    print('2. Mark tasks as complete')
    print('3. List all tasks')
    print('4. Display only incomplete tasks')
    print('5. Quit')

def main():
    todo=ToDOlist()

    while True:
        print_menu()
        choise = input('Chose one optipn(1-5): ').strip()

        if choise=='1':
            title= input('Enter title of task: ')
            description = input('Enter description: ')
            due_date = input("Enter due date (e.g. 2025-05-31): ")
            task = Task(title, description,due_date)
            todo.add_task(task)
            
        elif choise=='2':
            todo.list_all_tasks()
            index = int(input('Enter the task that is complete: '))
            todo.mark_complited(index)
        
        elif choise=='3':
            todo.list_all_tasks()

        elif choise =='4':
            todo.list_imcomplete_tasks()

        elif choise=='5':
            print('Programm is closed')
            break
    

if __name__=='__main__':
    main()



class Post:
    def __init__(self, title, content, author):
        self.title= title
        self.content=content,
        self.author= author
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\n, Author: {self.author}"

class Blog(Post):
    def __init__(self):
        self.posts=[]
    def add(self,post):
        self.posts.append(post)
    def list_all_posts(self):
        for i, post in enumerate(self.posts):
            print(f'\nPost {i}:{post}')
    def display_post_by_author(self, author_name):
        found = False
        for i in self.posts:
            if Post.author.lower()==author_name.lower():
                print(i)
                found=True
        if not found:
            print(f'No post from {author_name}')
    def delete_post(self,index):
        print(self.posts)
        if 0<=index <len(self.posts):
            delete = self.posts.pop(index)
            print(f'Deleted post titled {delete.title}')
        else:
            print('Invalid post number')
    def edit_post(self,index, new_title, new_content):
        if 0<=index<len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content= new_content
            print('Post updated successfully')
    def show_latest_post(self):
        if self.posts:
            print(self.posts[-1])
        else:
            print('No posts available.')
    def __repr__(self):
        return f'The {self.title}: {self.content}. By {self.author}'

       

def print_menu():   
    print('---Blog menu---')
    print('1. Add post')
    print('2. List all posts')
    print('3. Display post by author')
    print('4. Delete a post')
    print('5. Edit a post')
    print('6. Display latest post')
    print('7. Exit')

def main():
    blog=Blog()

    while True:
        print_menu()
        choise = input('Choise one option(1-5): ').strip()

        if choise=='1':
            title = input('Enter post title: ')
            content = input('Enter post: ')
            author = input('Your name: ')
            post = Post(title, content,author)
            blog.add(post)
        elif choise =='2':
            blog.list_all_posts()
        elif choise=='3':
            user_author = input('Enter author name: ')
            blog.display_post_by_author(user_author)
        elif choise =='4':
            blog.list_all_posts()
            index= int(input('Enter post number to delete'))
            blog.delete_post(index)
        elif choise=='5':
            blog.list_all_posts()
            index = int(input('Enter post number to edit: '))
            new_title = input('Enter new title: ')
            new_content = input('Enter new content: ')
            blog.edit_post(index,new_title, new_content)
        elif choise =='6':
            blog.show_latest_post()
        elif choise=='7':
            print('Programm is closed')
            break

if __name__=='__main__':
    main()
