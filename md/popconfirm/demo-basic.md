## zh-CN

最简单的用法，支持确认标题和描述。

> `description` 在 `5.1.0` 版本中支持。

## en-US

The basic example supports the title and description props of confirmation.

> `description` is supported in version `5.1.0`.
```tsx
import React from 'react';
import { Button, message, Popconfirm } from 'antd';

const confirm = (e: React.MouseEvent<HTMLElement>) => {
  console.log(e);
  message.success('Click on Yes');
};

const cancel = (e: React.MouseEvent<HTMLElement>) => {
  console.log(e);
  message.error('Click on No');
};

const App: React.FC = () => (
  <Popconfirm
    title="Delete the task"
    description="Are you sure to delete this task?"
    onConfirm={confirm}
    onCancel={cancel}
    okText="Yes"
    cancelText="No"
  >
    <Button danger>Delete</Button>
  </Popconfirm>
);

export default App;
```
