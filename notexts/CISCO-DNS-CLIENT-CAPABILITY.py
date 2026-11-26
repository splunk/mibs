#
# PySNMP MIB module CISCO-DNS-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DNS-CLIENT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDNSClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 888))
ciscoDNSClientCapability.setRevisions(('2004-11-25 00:00', '2004-08-10 00:00',))
if mibBuilder.loadTexts: ciscoDNSClientCapability.setLastUpdated('200411250000Z')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setOrganization('Cisco Systems, Inc.')
cDNSClientCapSanOSV20R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 888, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setProductRelease('Cisco SanOS 2.0(1) on Cisco MDS 9000\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-DNS-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDNSClientCapability, cDNSClientCapSanOSV20R1MDS9000=cDNSClientCapSanOSV20R1MDS9000, ciscoDNSClientCapability=ciscoDNSClientCapability)
