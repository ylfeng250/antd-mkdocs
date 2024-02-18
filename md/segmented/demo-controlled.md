## zh-CN

受控的 Segmented。

## en-US

Controlled Segmented.
```tsx
import React, { useState } from 'react';
import { Segmented } from 'antd';

const Demo: React.FC = () => {
  const [value, setValue] = useState<string | number>('Map');

  return <Segmented options={['Map', 'Transit', 'Satellite']} value={value} onChange={setValue} />;
};

export default Demo;
```
