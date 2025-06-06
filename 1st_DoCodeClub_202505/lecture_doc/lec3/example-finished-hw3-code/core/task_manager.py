import re
from datetime import datetime

class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.status = "pending"
        self.result = None
        self.created_at = datetime.now()
        self.completed_at = None
        self.failed_at = None
        self.error = None
        
    def mark_completed(self, result=None):
        """标记任务为已完成"""
        self.status = "completed"
        self.completed_at = datetime.now()
        self.result = result
        print(f"任务 {self.id} 已完成")
        
    def mark_failed(self, error=None):
        """标记任务为失败"""
        self.status = "failed"
        self.failed_at = datetime.now()
        self.error = error
        print(f"任务 {self.id} 执行失败: {error}")
        
    def to_dict(self):
        """转换为字典表示"""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "result": self.result,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "failed_at": self.failed_at.isoformat() if self.failed_at else None,
            "error": self.error
        }
        
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        
    def add_task(self, description):
        """添加新任务"""
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"创建新任务 {task.id}: {description}")
        return task
        
    def get_task(self, task_id):
        """获取指定ID的任务"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
        
    def get_all_tasks(self):
        """获取所有任务"""
        return self.tasks
        
    def get_pending_tasks(self):
        """获取待处理的任务"""
        return [task for task in self.tasks if task.status == "pending"]
        
    def get_completed_tasks(self):
        """获取已完成的任务"""
        return [task for task in self.tasks if task.status == "completed"]
        
    def clear_tasks(self):
        """清空所有任务"""
        self.tasks = []
        self.next_id = 1
        print("所有任务已清空")