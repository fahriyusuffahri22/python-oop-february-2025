from typing import List, Any
from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    @staticmethod
    def edit(collection: List[Any], _id: int, *args: Any) -> None:
        for x in collection:
            if x.id == _id:
                x.edit(*args)
                return

    @staticmethod
    def delete(collection: List[Any], _id: int) -> None:
        for i in range(len(collection)):
            if collection[i].id == _id:
                collection.pop(i)
                return

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.edit(self.categories, category_id, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.edit(self.topics, topic_id, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.edit(self.documents, document_id, new_file_name)

    def delete_category(self, category_id: int) -> None:
        self.delete(self.categories, category_id)

    def delete_topic(self, topic_id: int) -> None:
        self.delete(self.topics, topic_id)

    def delete_document(self, document_id: int) -> None:
        self.delete(self.documents, document_id)

    def get_document(self, document_id: int) -> Document:
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return "\n".join(str(x) for x in self.documents)