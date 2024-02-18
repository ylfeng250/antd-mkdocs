## zh-CN

给数值添加动画进入效果，需要配合 [react-countup](https://www.npmjs.com/package/react-countup)。

## en-US

Animated number with [react-countup](https://www.npmjs.com/package/react-countup).
```tsx
import React from 'react';
import CountUp from 'react-countup';
import { Col, Row, Statistic } from 'antd';

const formatter = (value: number) => <CountUp end={value} separator="," />;

const App: React.FC = () => (
  <Row gutter={16}>
    <Col span={12}>
      <Statistic title="Active Users" value={112893} formatter={formatter} />
    </Col>
    <Col span={12}>
      <Statistic title="Account Balance (CNY)" value={112893} precision={2} formatter={formatter} />
    </Col>
  </Row>
);

export default App;
```
