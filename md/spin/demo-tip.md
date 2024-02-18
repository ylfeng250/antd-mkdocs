## zh-CN

自定义描述文案。

## en-US

```css
.content {
  padding: 50px;
  background: rgba(0, 0, 0, 0.05);
  border-radius: 4px;
}
```
```tsx
import React from 'react';
import { Alert, Flex, Spin } from 'antd';

const App: React.FC = () => (
  <Flex gap="small" vertical>
    <Flex gap="small">
      <Spin tip="Loading" size="small">
        <div className="content" />
      </Spin>
      <Spin tip="Loading">
        <div className="content" />
      </Spin>
      <Spin tip="Loading" size="large">
        <div className="content" />
      </Spin>
    </Flex>
    <Spin tip="Loading...">
      <Alert
        message="Alert message title"
        description="Further details about the context of this alert."
        type="info"
      />
    </Spin>
  </Flex>
);

export default App;
```
