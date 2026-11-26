#
# PySNMP MIB module CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
ciscoIpslaVideoProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 605))
ciscoIpslaVideoProfileCapability.setRevisions(('2011-06-01 00:00',))
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setLastUpdated('201106010000Z')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpslaVideoProfileCapabilityV152R02T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 605, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY", ciscoIpslaVideoProfileCapability=ciscoIpslaVideoProfileCapability, ciscoIpslaVideoProfileCapabilityV152R02T=ciscoIpslaVideoProfileCapabilityV152R02T, PYSNMP_MODULE_ID=ciscoIpslaVideoProfileCapability)
