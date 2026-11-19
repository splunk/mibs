#
# PySNMP MIB module CISCO-CCM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CCM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:21 2026
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
ciscoCCMCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 211))
ciscoCCMCapability.setRevisions(('2011-06-14 00:00', '2009-12-15 00:00', '2008-08-21 00:00', '2008-02-20 00:00', '2005-11-21 00:00', '2003-10-03 00:00', '2002-03-21 00:00', '2001-07-02 00:00', '2001-06-19 00:00',))
if mibBuilder.loadTexts: ciscoCCMCapability.setLastUpdated('201106140000Z')
if mibBuilder.loadTexts: ciscoCCMCapability.setOrganization('Cisco Systems, Inc.')
ciscoCCMCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R00 = ciscoCCMCapabilityV3R00.setProductRelease('Cisco Call Manager 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R00 = ciscoCCMCapabilityV3R00.setStatus('current')
ciscoCCMCapabilityV3R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R01 = ciscoCCMCapabilityV3R01.setProductRelease('Cisco Call Manager 3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R01 = ciscoCCMCapabilityV3R01.setStatus('current')
ciscoCCMCapabilityV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03 = ciscoCCMCapabilityV3R03.setProductRelease('Cisco Call Manager 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03 = ciscoCCMCapabilityV3R03.setStatus('obsolete')
ciscoCCMCapabilityV3R03Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03Rev1 = ciscoCCMCapabilityV3R03Rev1.setProductRelease('Cisco Call Manager 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03Rev1 = ciscoCCMCapabilityV3R03Rev1.setStatus('current')
ciscoCCMCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV4R00 = ciscoCCMCapabilityV4R00.setProductRelease('Cisco Call Manager 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV4R00 = ciscoCCMCapabilityV4R00.setStatus('current')
ciscoCCMCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV5R00 = ciscoCCMCapabilityV5R00.setProductRelease('Cisco Call Manager 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV5R00 = ciscoCCMCapabilityV5R00.setStatus('current')
ciscoCCMCapabilityV7R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R00 = ciscoCCMCapabilityV7R00.setProductRelease('Cisco Unified Communications Manager 7.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R00 = ciscoCCMCapabilityV7R00.setStatus('current')
ciscoCCMCapabilityV7R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R01 = ciscoCCMCapabilityV7R01.setProductRelease('Cisco Unified Communications Manager 7.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R01 = ciscoCCMCapabilityV7R01.setStatus('current')
ciscoCCMCapabilityV8R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R00 = ciscoCCMCapabilityV8R00.setProductRelease('Cisco Unified Communications Manager 8.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R00 = ciscoCCMCapabilityV8R00.setStatus('current')
ciscoCCMCapabilityV8R05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R05 = ciscoCCMCapabilityV8R05.setProductRelease('Cisco Unified Communications Manager 8.5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R05 = ciscoCCMCapabilityV8R05.setStatus('current')
mibBuilder.exportSymbols("CISCO-CCM-CAPABILITY", ciscoCCMCapabilityV4R00=ciscoCCMCapabilityV4R00, ciscoCCMCapabilityV8R05=ciscoCCMCapabilityV8R05, ciscoCCMCapabilityV8R00=ciscoCCMCapabilityV8R00, PYSNMP_MODULE_ID=ciscoCCMCapability, ciscoCCMCapabilityV3R01=ciscoCCMCapabilityV3R01, ciscoCCMCapabilityV5R00=ciscoCCMCapabilityV5R00, ciscoCCMCapabilityV3R03Rev1=ciscoCCMCapabilityV3R03Rev1, ciscoCCMCapabilityV7R00=ciscoCCMCapabilityV7R00, ciscoCCMCapabilityV3R00=ciscoCCMCapabilityV3R00, ciscoCCMCapabilityV3R03=ciscoCCMCapabilityV3R03, ciscoCCMCapability=ciscoCCMCapability, ciscoCCMCapabilityV7R01=ciscoCCMCapabilityV7R01)
