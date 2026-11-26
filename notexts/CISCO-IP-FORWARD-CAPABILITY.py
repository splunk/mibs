#
# PySNMP MIB module CISCO-IP-FORWARD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-FORWARD-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpForwardCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 595))
ciscoIpForwardCapability.setRevisions(('2010-09-23 00:00',))
if mibBuilder.loadTexts: ciscoIpForwardCapability.setLastUpdated('201009230000Z')
if mibBuilder.loadTexts: ciscoIpForwardCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpForwardCapabilityV12R2SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 595, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpForwardCapabilityV12R2SE = ciscoIpForwardCapabilityV12R2SE.setProductRelease('Cisco IOS 12.2SE Catalyst 2k/3k series.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpForwardCapabilityV12R2SE = ciscoIpForwardCapabilityV12R2SE.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-FORWARD-CAPABILITY", ciscoIpForwardCapability=ciscoIpForwardCapability, ciscoIpForwardCapabilityV12R2SE=ciscoIpForwardCapabilityV12R2SE, PYSNMP_MODULE_ID=ciscoIpForwardCapability)
