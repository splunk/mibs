#
# PySNMP MIB module CISCOSB-Dlf-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-Dlf-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlDlf = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 135))
if mibBuilder.loadTexts: rlDlf.setLastUpdated('200809151234Z')
if mibBuilder.loadTexts: rlDlf.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlDlf.setContactInfo('Postal: 170 West Tasman Drive\n        San Jose , CA 95134-1706\n        USA\n\n        \n        Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlDlf.setDescription('The private MIB module definition for DLF Ports MIB.\n             unknown unicast egress filtering ')
rlDlfPortList = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 135, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDlfPortList.setStatus('current')
if mibBuilder.loadTexts: rlDlfPortList.setDescription('A port bitmap containing entries of unknown unicas egress filtering')
mibBuilder.exportSymbols("CISCOSB-Dlf-MIB", PYSNMP_MODULE_ID=rlDlf, rlDlf=rlDlf, rlDlfPortList=rlDlfPortList)
