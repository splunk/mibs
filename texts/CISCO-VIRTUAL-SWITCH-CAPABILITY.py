#
# PySNMP MIB module CISCO-VIRTUAL-SWITCH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VIRTUAL-SWITCH-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoVirtualSwitchCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 563))
ciscoVirtualSwitchCapability.setRevisions(('2012-09-07 00:00', '2011-09-26 00:00', '2010-03-29 00:00', '2008-01-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setRevisionsDescriptions(('Added capability statement cvsCapV15R0101SYPCat6K.', 'Added capability statement cvsCapV15R0001SYPCat6K.', 'Added capability statement cvsCapV12R0233SXI4PCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setDescription('The Agent capabilities for CISCO-VIRTUAL-SWITCH-MIB.')
cvsCapV12R0233SXH01PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXH01PCat6K = cvsCapV12R0233SXH01PCat6K.setProductRelease('Cisco IOS 12.2(33)SXH1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXH01PCat6K = cvsCapV12R0233SXH01PCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV12R0233SXH01PCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
cvsCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXI4PCat6K = cvsCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXI4PCat6K = cvsCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV12R0233SXI4PCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
cvsCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0001SYPCat6K = cvsCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0001SYPCat6K = cvsCapV15R0001SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV15R0001SYPCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
cvsCapV15R0101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0101SYPCat6K = cvsCapV15R0101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0101SYPCat6K = cvsCapV15R0101SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV15R0101SYPCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VIRTUAL-SWITCH-CAPABILITY", PYSNMP_MODULE_ID=ciscoVirtualSwitchCapability, cvsCapV12R0233SXI4PCat6K=cvsCapV12R0233SXI4PCat6K, cvsCapV15R0101SYPCat6K=cvsCapV15R0101SYPCat6K, cvsCapV12R0233SXH01PCat6K=cvsCapV12R0233SXH01PCat6K, ciscoVirtualSwitchCapability=ciscoVirtualSwitchCapability, cvsCapV15R0001SYPCat6K=cvsCapV15R0001SYPCat6K)
