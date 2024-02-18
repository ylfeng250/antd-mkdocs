## zh-CN

警告类型的结果。

## en-US

The result of the warning.
```tsx
import React from 'react';
import { Button, Result } from 'antd';

const App: React.FC = () => (
  <Result
    status="warning"
    title="There are some problems with your operation."
    extra={
      <Button type="primary" key="console">
        Go Console
      </Button>
    }
  />
);

export default App;
```
