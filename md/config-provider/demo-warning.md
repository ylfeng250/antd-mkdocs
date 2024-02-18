## zh-CN

调整 warning 策略。

## en-US

Adjust warning strategy.
```tsx
import React from 'react';
import { Alert, ConfigProvider, Input, Typography } from 'antd';

const App: React.FC = () => (
  <>
    <Typography.Title level={4}>Open single page to check the console</Typography.Title>
    <ConfigProvider warning={{ strict: false }}>
      <Alert closeText="deprecated" />
      <Input.Group />
    </ConfigProvider>
  </>
);

export default App;
```
