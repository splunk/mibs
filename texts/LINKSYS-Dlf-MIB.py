#
# PySNMP MIB module LINKSYS-Dlf-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-Dlf-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:12:02 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, Gauge32, Unsigned32, NotificationType, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, MibIdentifier, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Gauge32", "Unsigned32", "NotificationType", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "MibIdentifier", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlDlf = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 135))
if mibBuilder.loadTexts: rlDlf.setLastUpdated('200809151234Z')
if mibBuilder.loadTexts: rlDlf.setOrganization('Linksys LLC.')
if mibBuilder.loadTexts: rlDlf.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlDlf.setDescription('The private MIB module definition for DLF Ports MIB.\n             unknown unicast egress filtering ')
rlDlfPortList = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 135, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDlfPortList.setStatus('current')
if mibBuilder.loadTexts: rlDlfPortList.setDescription('A port bitmap containing entries of unknown unicas egress filtering')
mibBuilder.exportSymbols("LINKSYS-Dlf-MIB", PYSNMP_MODULE_ID=rlDlf, rlDlf=rlDlf, rlDlfPortList=rlDlfPortList)
