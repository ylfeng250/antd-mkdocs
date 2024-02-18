## zh-CN

修改组件和图标前缀。

## en-US

Config component and icon prefixCls.
```tsx
import { SmileOutlined } from '@ant-design/icons';
import React, { useState } from 'react';
import { Button, ConfigProvider, Select } from 'antd';

// Ant Design site use `es` module for view
// but do not replace related lib `lib` with `es`
// which do not show correct in site.
// We may need do convert in site also.
const App: React.FC = () => {
  const [prefixCls, setPrefixCls] = useState('light');
  return (
    <>
      <Button style={{ marginBottom: '12px' }} type="primary" onClick={() => setPrefixCls('dark')}>
        toggle prefixCls
      </Button>
      <br />
      <ConfigProvider prefixCls={prefixCls} iconPrefixCls="bamboo">
        <SmileOutlined />
        <Select style={{ width: 120 }} />
      </ConfigProvider>
    </>
  );
};

export default App;
```
