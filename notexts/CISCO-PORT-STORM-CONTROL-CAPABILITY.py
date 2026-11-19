#
# PySNMP MIB module CISCO-PORT-STORM-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PORT-STORM-CONTROL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPortStormControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 542))
ciscoPortStormControlCapability.setRevisions(('2014-04-04 00:00', '2012-09-07 00:00', '2011-03-24 00:00', '2007-07-03 00:00', '2007-07-02 00:00',))
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setOrganization('Cisco Systems, Inc.')
cpscCapabilityV12R0240SGCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0240SGCat4K = cpscCapabilityV12R0240SGCat4K.setProductRelease('Cisco IOS 12.2(40)SG on Cat4K platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0240SGCat4K = cpscCapabilityV12R0240SGCat4K.setStatus('current')
cpscCapabilityV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXHPCat6K = cpscCapabilityV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXHPCat6K = cpscCapabilityV12R0233SXHPCat6K.setStatus('current')
cpscCapabilityV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXJPCat6k = cpscCapabilityV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXJPCat6k = cpscCapabilityV12R0233SXJPCat6k.setStatus('current')
cpscCapabilityV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV15R0101SYPCat6k = cpscCapabilityV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV15R0101SYPCat6k = cpscCapabilityV15R0101SYPCat6k.setStatus('current')
cpscCapabilityV06R0002U0301PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV06R0002U0301PN3K = cpscCapabilityV06R0002U0301PN3K.setProductRelease('Cisco NX-OS 6.0(2)U3(1) on Nexus 3000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV06R0002U0301PN3K = cpscCapabilityV06R0002U0301PN3K.setStatus('current')
mibBuilder.exportSymbols("CISCO-PORT-STORM-CONTROL-CAPABILITY", ciscoPortStormControlCapability=ciscoPortStormControlCapability, PYSNMP_MODULE_ID=ciscoPortStormControlCapability, cpscCapabilityV12R0233SXHPCat6K=cpscCapabilityV12R0233SXHPCat6K, cpscCapabilityV15R0101SYPCat6k=cpscCapabilityV15R0101SYPCat6k, cpscCapabilityV06R0002U0301PN3K=cpscCapabilityV06R0002U0301PN3K, cpscCapabilityV12R0233SXJPCat6k=cpscCapabilityV12R0233SXJPCat6k, cpscCapabilityV12R0240SGCat4K=cpscCapabilityV12R0240SGCat4K)
